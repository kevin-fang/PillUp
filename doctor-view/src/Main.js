import React from 'react'
import { Switch, Route } from 'react-router-dom'

import { HomePageComponent } from './components/HomePageComponent.js'
import { PatientDisplayComponent } from './components/PatientDisplayComponent.js'

export default class Main extends React.Component {
	render() {
		return (
			<main>
	          <Switch>
	            <Route exact path='/' component={HomePageComponent} />
	            <Route exact path='/patient' component={PatientDisplayComponent} />
	          </Switch>
        	</main>
        	)
	}
}