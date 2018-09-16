import React from 'react'
import { Switch, Route } from 'react-router-dom'

import { HomePageComponent } from './components/HomePageComponent.js'
import { PatientDisplayComponent } from './components/PatientDisplayComponent.js'
import { AboutComponent } from './components/AboutComponent.js'
export default class Main extends React.Component {
	constructor(props) {
		super(props)
	}

	render() {
		return (
			<main>
	          <Switch>
	            <Route exact path='/' component={HomePageComponent} />
	            <Route exact path='/patient' component={PatientDisplayComponent} />
	            <Route exact path='/about' component={AboutComponent} />
	          </Switch>
        	</main>
        	)
	}
}