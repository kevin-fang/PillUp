from datetime import datetime, timedelta
import requests
from enum import Enum
import json
import re


# todo Appearance: https://documentation.onesignal.com/reference#section-appearance
# todo Grouping and Collapsing: https://documentation.onesignal.com/reference#section-grouping-collapsing


class _LangCodes:
    """LangCodes Class"""

    def load(self, filename):
        """ loads lang codes from json file """
        data = json.loads(open(filename, 'r').read())
        for key, info in data.items():
            setattr(self, info['name'], key)
        return self


# load language codes from json file
LangCodes = _LangCodes().load('lang_codes.json')


class Relation(Enum):
    GreaterThan = '>'
    LowerThan = '<'
    Equal = '='
    NotEqual = '!='
    Exists = 'exists'
    NotExists = 'not_exists'


class DelayedOption(Enum):
    Timezone = 'timezone'
    LastActive = 'last-active'


class Delivery:
    def __init__(self):
        self._data = {}

    def send_after(self, date: datetime):
        """
        Schedule notification for future delivery.
        :param date: future date
        """
        if date < datetime.now():
            raise Exception('date cannot be in the past')

        self._data['send_after'] = date.strftime('%Y-%m-%d %H:%M:%S GMT-0000')
        return self

    def delayed_option(self, option: DelayedOption):
        """
        Options:
        timezone (Deliver at a specific time-of-day in each users own timezone)
        last-active Same as Intelligent Delivery . (Deliver at the same time of day as each user last used your app).
        If send_after is used, this takes effect after the send_after time has elapsed.
        :param option: delay option
        """
        self._data['delayed_option'] = option.value
        return self

    def delivery_time_of_day(self, time: str):
        """
        used with DelayedOption.timezone
        :param time: time of day "9:00AM"
        """
        self._data['delivery_time_of_day'] = time
        return self

    def time_to_live(self, seconds: int, delta: timedelta = None):
        """
        Time To Live - In seconds. The notification will be expired if the device
        does not come back online within this time. The default is 259,200 seconds (3 days).
        Max value to set is 2419200 seconds (28 days).
        :param seconds: number of seconds
        :param delta: optional time delta
        """

        total_seconds = seconds if seconds is not None else 0
        total_seconds += delta.seconds if delta is not None else 0
        self._data['ttl'] = total_seconds
        return self

    def priority(self, priority: int):
        """
        Delivery priority through the push server (example GCM/FCM). Pass 10 for high priority.
        Defaults to normal priority for Android and high for iOS. For Android 6.0+ devices
        setting priority to high will wake the device out of doze mode.
        :param priority: notification priority
        """

        self._data['priority'] = priority
        return self

    @property
    def data(self):
        """ :return: delivery data as json """
        return self._data


class Buttons:
    def __init__(self):
        self._buttons = []
        self._web_buttons = []

    def add_button(self, id: str, text: str, icon: str = None):
        """
        Add a new action button
        :param id: button's id
        :param text: button's text
        :param icon: optional button icon (Only works for android)
        """
        self._buttons.append({'id': id, 'text': text, 'icon': icon})
        return self

    def add_web_buttons(self, id: str, text: str, icon: str, url: str):
        """
        Add a new web action button
        :param id: button's id
        :param text: button's text
        :param icon: button's icon
        :param url: redirection url
        """
        self._web_buttons.append({'id': id, 'text': text,
                                  'icon': icon, 'url': url})
        return self

    @property
    def buttons_json(self):
        return json.dumps(self._buttons)

    @property
    def buttons(self):
        return self._buttons

    @property
    def web_buttons_json(self):
        return json.dumps(self._web_buttons)

    @property
    def web_buttons(self):
        return self._web_buttons


class Filter:
    def __init__(self):
        """ initiate a new Filter """
        self._data = []

    @staticmethod
    def accepts(relations: [Relation], provided: Relation):
        """
        check to see whether a provided relation is acceptable
        :param relations: list of accepted relations
        :param provided: the provided relation
        """
        if not any([provided == relation for relation in relations]):
            raise Exception('Invalid relation was provided')
        return True

    def _base_filter(self, field, relation: Relation, value, key=None):
        """
        base filter generator
        :param field: field name
        :param relation: filter's relation
        :param value: filter's value
        :param key: optional filter key
        """
        json_data = {'field': field, 'relation': relation.value, 'value': value}
        if key:
            json_data['key'] = key
        self._data.append(json_data)
        return self

    def last_session(self, relation: Relation, hours_ago: float):
        """
        :param relation: ">" or "<"
        :param hours_ago: number of hours before or after the users last session.
        """
        Filter.accepts([Relation.GreaterThan, Relation.LowerThan], relation)
        return self._base_filter('last_session', relation, hours_ago)

    def first_session(self, relation: Relation, hours_ago: float):
        """
        :param relation: ">" or "<"
        :param hours_ago: number of hours before or after the users first session.
        """
        Filter.accepts([Relation.GreaterThan, Relation.LowerThan], relation)
        return self._base_filter('first_session', relation, hours_ago)

    def session_count(self, relation: Relation, count: int):
        """
        :param relation: ">", "<", "=" or "!="
        :param count: number of sessions
        """
        Filter.accepts([Relation.GreaterThan, Relation.LowerThan,
                        Relation.Equal, Relation.NotEqual], relation)
        return self._base_filter('session_count', relation, count)

    def session_time(self, relation: Relation, seconds: int):
        """
        :param relation: ">", "<"
        :param seconds: time in seconds the user has been in your app
        """
        Filter.accepts([Relation.GreaterThan, Relation.LowerThan], relation)
        return self._base_filter('session_time', relation, seconds)

    def amount_spent(self, relation: Relation, amount: float):
        """
        :param relation: ">", "<" or "="
        :param amount: Amount in USD a user has spent on IAP
        """
        Filter.accepts([Relation.GreaterThan, Relation.LowerThan,
                        Relation.Equal], relation)
        return self._base_filter('amount_spent', relation, amount)

    def bought_sku(self, key: str, relation: Relation, amount: float):
        """
        :param key: SKU purchased in your app as IAP
        :param relation: ">", "<", "="
        :param amount: value of SKU to compare to
        """
        Filter.accepts([Relation.GreaterThan, Relation.LowerThan,
                        Relation.Equal], relation)
        self._base_filter(key, relation, amount)

    def tag(self, key: str, relation: Relation, value: str):
        """
        Note: value is not required for "exists or "not_exists"
        :param key: tag key to compare to
        :param relation: ">", "<", "=", "!=", "exists", "not_exists"
        :param value: Tag value to compare to
        """
        self._base_filter('tag', relation, value, key=key)

    def language(self, relation: Relation, lang: str):
        """
        :param relation: "=", "!="
        :param lang: 2 character lang code
        """
        Filter.accepts([Relation.Equal, Relation.NotEqual], relation)
        self._base_filter('language', relation, lang)

    def app_version(self, relation: Relation, version: str):
        """
        :param relation: ">", "<", "=", "!="
        :param version:  app version
        """
        Filter.accepts([Relation.GreaterThan, Relation.LowerThan,
                        Relation.Equal, Relation.NotEqual], relation)
        self._base_filter('app_version', relation, version)

    def location(self, radius: float, lat: float, long: float):
        """
        :param radius: radius in meters
        :param lat: latitude
        :param long: longitude
        """
        self._data.append({'radius': radius, 'lat': lat, 'long': long})
        return self

    def country(self, country_code: str):
        """
        Relation is always '='
        :param country_code: 2-digit country code
        """
        return self._base_filter('country', Relation.Equal, country_code)

    @property
    def and_(self):
        """ appends And between the previous and next entries """
        self._data.append({'operator': 'AND'})
        return self

    @property
    def or_(self):
        """ appends Or between the previous and next entries """
        self._data.append({'operator': 'OR'})
        return self

    @property
    def data(self):
        return self._data

    def to_json(self):
        """ :return: json formatter filter """
        return json.dumps(self._data)


class TargetDevice:
    def __init__(self):
        self._data = {}

    def include_player_ids(self, tokens: [str]):
        """
        Set specific players to send your notification to
        :param tokens: specific player ids
        """

        if len(tokens) > 2000:
            raise Exception('Exceeded the limit of 2000 per api call')
        self._data['include_player_ids'] = tokens
        return self

    def include_ios_tokens(self, tokens: [str]):
        """
        Please consider using include_player_ids instead
        Target using iOS device tokens. Warning: Only works with Production tokens.
        :param tokens: iOS device tokens
        """

        if len(tokens) > 2000:
            raise Exception('Exceeded the limit of 2000 per api call')
        # removing all non alphanumerical characters
        tokens = map(lambda x: re.sub(r'\W+', '', x), tokens)
        self._data['include_ios_tokens'] = tokens
        return self

    def include_wp_wns_uris(self, tokens: [str]):
        """
        Please consider using include_player_ids instead
        Target using Windows URIs.
        If a token does not correspond to an existing user, a new user will be created
        :param tokens: Windows URIs
        """
        if len(tokens) > 2000:
            raise Exception('Exceeded the limit of 2000 per api call')
        self._data['include_wp_wns_uris'] = tokens
        return self

    def include_amazon_reg_ids(self, tokens: [str]):
        """
        Please consider using include_player_ids instead
        Target using Amazon ADM registration IDs.
        If a token does not correspond to an existing user, a new user will be created.
        :param tokens: Amazon ADM registration IDs
        """
        if len(tokens) > 2000:
            raise Exception('Exceeded the limit of 2000 per api call')
        self._data['include_amazon_reg_ids'] = tokens
        return self

    def include_chrome_reg_ids(self, tokens: [str]):
        """
        Please consider using include_player_ids instead
        Target using Chrome App registration IDs.
        If a token does not correspond to an existing user, a new user will be created
        :param tokens:
        """
        if len(tokens) > 2000:
            raise Exception('Exceeded the limit of 2000 per api call')
        self._data['include_chrome_reg_ids'] = tokens
        return self

    def include_chrome_web_reg_ids(self, tokens: [str]):
        """
        Please consider using include_player_ids instead
        Target using Chrome Web Push registration IDs.
        If a token does not correspond to an existing user, a new user will be created.
        :param tokens: Chrome Web Push registration IDs
        """
        if len(tokens) > 2000:
            raise Exception('Exceeded the limit of 2000 per api call')
        self._data['include_chrome_web_reg_ids'] = tokens
        return self

    def include_android_reg_ids(self, tokens: [str]):
        """
        Please consider using include_player_ids instead
        Target using Android device registration IDs.
        If a token does not correspond to an existing user, a new user will be created.
        :param tokens: Android device registration IDs
        """
        if len(tokens) > 2000:
            raise Exception('Exceeded the limit of 2000 per api call')
        self._data['include_android_reg_ids'] = tokens
        return self

    @property
    def data(self):
        return self._data

    def to_json(self):
        """ :return: json formatted TargetDevice """
        return json.dumps(self._data)


class Notification:
    def __init__(self):
        self._data = {}

    def add_filters(self, filters: Filter):
        """
        add user targeting filters
        :param filters: filter instance
        """
        self._data['filters'] = filters.data
        return self

    @property
    def filters(self):
        """ Get filters """
        return self._data.get('filters')

    @filters.setter
    def filters(self, filters: Filter):
        """
        add user targeting filters
        :param filters: filter instance
        """
        self._data['filters'] = filters.to_json()

    def add_segments(self, segments: [str]):
        """
        add target segments
        :param segments: list of segments
        """
        self._data['included_segments'] = segments
        return self

    @property
    def segments(self):
        """ Get targeted segments """
        return self._data.get('included_segments')

    @segments.setter
    def segments(self, segments: [str]):
        """
        add target segments
        :param segments: list of segments
        """
        self._data['included_segments'] = segments

    def add_content(self, lang_code: str, message: str):
        """
        The notification's content (excluding the title),
        a map of language codes to text for each language.
        :param lang_code: language code string
        :param message: localized text
        """
        if not hasattr(self._data, 'contents'):
            self._data['contents'] = {}

        self._data['contents'][lang_code] = message
        return self

    def add_contents(self, json_content: dict):
        """
        The notification's content (excluding the title),
        a map of language codes to text for each language.
        :param json_content: add bulk json content
        Example: {"en": "English Message", "es": "Spanish Message"}
        """
        if not hasattr(self._data, 'contents'):
            self._data['contents'] = {}

        data = self._data['contents'].items() + json_content.items()
        self._data['contents'] = dict(data)
        return self

    @property
    def contents(self):
        """ :return: The notification's content (excluding the title),
        a map of language codes to text for each language. """

        return self._data.get('content')

    @contents.setter
    def contents(self, json_content):
        """
        The notification's content (excluding the title),
        a map of language codes to text for each language.
        :param json_content: add bulk json content
        """
        self.add_contents(json_content)

    def add_heading(self, lang_code: str, heading: str):
        """
        The notification's title, a map of language codes to text for each language
        :param lang_code: language code string
        :param heading: localized text
        """
        if not hasattr(self._data, 'headings'):
            self._data['headings'] = {}

        self._data['headings'][lang_code] = heading
        return self

    def add_headings(self, json_heading: dict):
        """
        The notification's title, a map of language codes to text for each language
        :param json_heading: add bulk json heading
        Example: {"en": "English Title", "es": "Spanish Title"}
        """
        if not hasattr(self._data, 'headings'):
            self._data['headings'] = {}

        data = self._data['headings'].items() + json_heading.items()
        self._data['headings'] = dict(data)
        return self

    @property
    def headings(self):
        """ :return: The notification's title, a map
        of language codes to text for each language """
        return self._data.get('headings')

    @headings.setter
    def headings(self, json_heading: dict):
        """
        The notification's title, a map of language codes to text for each language
        :param json_heading: add bulk json heading
        Example: {"en": "English Title", "es": "Spanish Title"}
        """
        self.add_headings(json_heading)

    def add_subtitle(self, lang_code: str, subtitle: str):
        """
        The notification's subtitle, a map of language codes to text for each language.
        :param lang_code: language code string
        :param subtitle: localized text
        """
        if not hasattr(self._data, 'subtitle'):
            self._data['subtitle'] = {}

        self._data['subtitle'][lang_code] = subtitle
        return self

    def add_subtitles(self, json_subtitles: dict):
        """
        The notification's subtitle, a map of language codes to text for each language.
        :param json_subtitles: add bulk json heading
        Example: {"en": "English Subtitle", "es": "Spanish Subtitle"}
        """
        if not hasattr(self._data, 'subtitle'):
            self._data['subtitle'] = {}

        data = self._data['subtitle'].items() + json_subtitles.items()
        self._data['subtitle'] = dict(data)
        return self

    @property
    def subtitles(self):
        """ :return: The notification's subtitle, a map of
        language codes to text for each language. """
        return self._data.get('subtitles')

    @subtitles.setter
    def subtitles(self, json_subtitles: dict):
        """
        The notification's subtitle, a map of language codes to text for each language.
        :param json_subtitles: add bulk json heading
        Example: {"en": "English Subtitle", "es": "Spanish Subtitle"}
        """
        self.add_subtitles(json_subtitles)

    def set_content_available(self, value: bool):
        """ Sending true wakes your app from background to run custom native code """
        self._data['content_available'] = value
        return self

    @property
    def content_available(self):
        """ Sending true wakes your app from background to run custom native code """
        return self._data.get('content_available')

    @content_available.setter
    def content_available(self, value: bool):
        """ Sending true wakes your app from background to run custom native code """
        self._data['content_available'] = value

    def set_mutable_content(self, value: bool):
        """ Sending true allows you to change the notification
        content in your app before it is displayed. """
        self._data['mutable_content'] = value
        return self

    def add_data(self, data: dict):
        """
        :param data: A custom map of data that is passed back to your app
        Example: {"abc": "123", "foo": "bar"}
        """
        self._data['data'] = data
        return self

    @property
    def data(self):
        """:return: A custom map of data that is passed back to your app """
        return self._data

    @data.setter
    def data(self, data: dict):
        """
        :param data: A custom map of data that is passed back to your app
        Example: {"abc": "123", "foo": "bar"}
        """
        self.add_data(data)

    def add_url(self, url: str):
        """
        :param url: The URL to open in the browser when a user clicks on the notification.
        """
        self._data['url'] = url
        return self

    @property
    def url(self):
        """:return: The URL to open in the browser when a user clicks on the notification. """
        return self._data.get('url')

    @url.setter
    def url(self, url: str):
        """
        :param url: The URL to open in the browser when a user clicks on the notification.
        """
        self.add_url(url)

    def set_ios_attachments(self, attachments: dict):
        """
        Adds media attachments to notifications. Set as JSON object,
        key as a media id of your choice and the value as a valid
        local filename or URL. User must press and hold on the notification to view.
        :param attachments: attachments for your ios client
        Example: {"id1": "https://domain.com/image.jpg"}
        """
        self._data['ios_attachemtns'] = attachments
        return self

    @property
    def ios_attachments(self):
        """
        Adds media attachments to notifications. Set as JSON object,
        key as a media id of your choice and the value as a valid
        local filename or URL. User must press and hold on the notification to view.
        """
        return self._data.get('ios_attachments')

    @ios_attachments.setter
    def ios_attachments(self, attachments: dict):
        """
        Adds media attachments to notifications. Set as JSON object,
        key as a media id of your choice and the value as a valid
        local filename or URL. User must press and hold on the notification to view.
        :param attachments: attachments for your ios client
        Example: {"id1": "https://domain.com/image.jpg"}
        """
        self.set_ios_attachments(attachments)

    def set_big_picture(self, picture: str):
        """
        Picture to display in the expanded view.
        :param picture: Picture to display in the expanded view.
        """
        self._data['big_picture'] = picture
        return self

    @property
    def big_picture(self):
        """ :return: Picture to display in the expanded view."""
        return self._data.get('big_picture')

    @big_picture.setter
    def big_picture(self, picture: str):
        """
        Picture to display in the expanded view.
        :param picture: Picture to display in the expanded view.
        """
        self.set_big_picture(picture)

    def set_adm_big_picture(self, picture: str):
        """
        Picture to display in the expanded view.
        :param picture: Picture to display in the expanded view.
        """
        self._data['adm_big_picture'] = picture
        return self

    @property
    def adm_big_picture(self):
        """
        Picture to display in the expanded view.
        :return: Picture to display in the expanded view.
        """
        return self._data.get('adm_big_picture')

    @adm_big_picture.setter
    def adm_big_picture(self, picture: str):
        """
        Picture to display in the expanded view.
        :param picture: Picture to display in the expanded view.
        """
        self.set_adm_big_picture(picture)

    def set_chrome_big_picture(self, picture: str):
        """
        Large picture to display below the notification text.
        :param picture: Must be a local URL.
        """
        self._data['chrome_big_picture'] = picture
        return self

    @property
    def chrome_big_picture(self):
        """ Large picture to display below the notification text. """
        return self._data.get('chrome_big_picture')

    @chrome_big_picture.setter
    def chrome_big_picture(self, picture: str):
        """
        Large picture to display below the notification text.
        :param picture: Must be a local URL.
        """
        self.set_chrome_big_picture(picture)

    def add_buttons(self, buttons: Buttons):
        """
        add buttons from the Button generator
        :param buttons: Buttons instance
        """

        if 'buttons' not in self._data:
            self._data['buttons'] = []
        if 'web_buttons' not in self._data:
            self._data['web_buttons'] = []

        self._data['buttons'] += buttons.buttons
        self._data['web_buttons'] += buttons.web_buttons
        return self

    def add_buttons_raw(self, json_data: dict):
        """
        add raw button data in json format
        :param json_data: button data
        """

        if 'buttons' not in self._data:
            self._data['buttons'] = []

        self._data['buttons'].append(json_data)
        return self

    def add_web_buttons_raw(self, json_data: dict):
        """
        add raw web button data in json format
        :param json_data: web button data
        """

        if 'web_buttons' not in self._data:
            self._data['web_buttons'] = []

        self._data['web_buttons'].append(json_data)
        return self

    def set_ios_category(self, category: str):
        """
        Category APS payload, use with registerUserNotificationSettings:categories
        in your Objective-C / Swift code. Example: in your Objective-C / Swift code.
        :param category: category payload
        """

        self._data['ios_category'] = category
        return self

    @property
    def ios_category(self):
        """
        Category APS payload, use with registerUserNotificationSettings:categories
        in your Objective-C / Swift code. Example: in your Objective-C / Swift code.
        """

        return self._data.get('ios_category')

    @ios_category.setter
    def ios_category(self, category: str):
        """
        Category APS payload, use with registerUserNotificationSettings:categories
        in your Objective-C / Swift code. Example: in your Objective-C / Swift code.
        :param category: category payload
        """

        self.set_ios_category(category)

    def set_delivery(self, delivery: Delivery):
        """
        set notification delivery option
        :param delivery: delivery instance
        """

        self._data = {**self._data, **delivery.data}
        return self

    def set_target_device(self, target: TargetDevice):
        """
        set targeted devices for this notification
        :param target: TargetDevice instance
        """

        self.data = {**self._data, **target.data}
        return self

    @property
    def data(self):
        return self._data

    def to_json(self):
        """ :return: json string representation of this notification"""
        return json.dumps(self._data)


class OneSignal:
    _url = 'https://onesignal.com/api/v1/notifications'

    def __init__(self, app_id: str, api_key: str):
        """
        Initiate a new notification center
        For app_id and api_key refer to: https://goo.gl/NzpytH
        :param app_id: onesignal's app id
        :param api_key: onesignal's rest api key
        """
        self._app_id = app_id
        self._api_key = api_key

    @staticmethod
    def _create_header(api_key):
        """
        create custom header for the api
        :param api_key: oensignal's api key
        :return: header in dict format
        """
        return {
            "Content-Type": "application/json",
            "Authorization": "Basic {}".format(api_key)
        }

    @staticmethod
    def _get(url: str, headers: dict):
        """
        make a get request
        :param url: endpoint url
        :param headers: request headers
        :return: json data
        """
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    @staticmethod
    def _post(url: str, headers: dict, payload: dict):
        """
        make a post request
        :param url: endpoint url
        :param headers: request headers
        :param payload: request payload
        :return: json data
        """
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()

    @staticmethod
    def _delete(url: str, headers: dict):
        """
        make a delete request
        :param url: endpoint url
        :param headers: request headers
        :return: json data
        """
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def post(self, notification: Notification):
        """
        submit a notification to the api
        :param notification: notification instance
        :return: (not decided yet)
        """
        payload = notification.data
        payload['app_id'] = self._app_id
        headers = OneSignal._create_header(self._api_key)
        return OneSignal._post(self._url, headers, payload)

    def cancel(self, notification_id: str):
        """
        cancel a notification using its notification id
        :param notification_id: notification's id
        :return: (not decided yet)
        """
        headers = OneSignal._create_header(self._api_key)
        url = self._url + "{}?app_id=[}".format(notification_id, self._app_id)
        return OneSignal._delete(url, headers)