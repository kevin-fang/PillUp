import React from 'react'

// list stuff
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';

let sampleData = require('../patients.json')

export class HomePageComponent extends React.Component {
	render = () => {
		let introStyle = {
			padding: 70,
			paddingBottom: 20,
			flex: 1,
			fontSize: 80, 
			fontColor: '#FF0000',
			backgroundColor: "#e6ffff",
			textAlign: 'center'
		}

		let patientListStyle = {
			padding: 10,
			paddingLeft: 0,
			fontSize: 40, 
			fontColor: '#FF0000',
			backgroundColor: "#e6eeff",
			textAlign: 'center'
		}
		return (
			<div>
				<div style={introStyle}>
					Welcome, Doctor Shayan
				</div>
				<div style={patientListStyle}>
					Patient Statuses
					<ul style={{listStyleType: 'none', width: "100%", padding: 8}}>
						{
							sampleData.patients.map((patient) => {
								return (
									<ListItem button>
										<ListItemText>{patient.name}</ListItemText>
									</ListItem>
									)
							})
						}
					</ul>
				</div>
			</div>
		)
	}
}