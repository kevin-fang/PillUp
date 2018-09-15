import React from 'react'

import Typography from '@material-ui/core/Typography'

// list imports
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';

// card imports
import Card from '@material-ui/core/Card';
import CardActionArea from '@material-ui/core/CardActionArea';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import Button from '@material-ui/core/Button';


import FlipMove from 'react-flip-move';

let sampleData = require('../patients.json')
sampleData.patients.sort((a, b) => {
	return a.name > b.name
})

export class HomePageComponent extends React.Component {

	generatePatientCard = (patient) => {
		return (
			<Card key={patient.name} style={{margin: 10, minWidth: 200}}>
				<div style={{}}>
					{/*<Typography className={{marginBottom: 16, fontSize: 14}} color="textSecondary">
						Welcome
					</Typography>*/}
					<CardMedia
					style={{height: 250, objectFit: 'cover'}}
					image={patient.image}
					title="Shayan"
					/>
					<CardContent>
						<Typography gutterBottom variant="headline" component="h2">
							{patient.name.split(' ')[0] + " "} 
							{patient.name.split(' ')[1]}
						</Typography>
						<Typography component="p">
							<b>Status:</b> {patient.status}
						</Typography>
					</CardContent>
					<CardActions style={{position: 'relative', bottom: 0}}>
						<Button onClick={this.displayCard} size="small" color="primary">
						  Patient Info
						</Button>
						<Button size="small" color="secondary">
						  Modify Prescription
						</Button>
					</CardActions>
				</div>
			</Card>
		)
	}
	render() {

		let patientListStyle = {
			paddingTop: 15,
			paddingLeft: 0,
			fontSize: 40, 
			height: "100%", 
			fontColor: '#FF0000',
			backgroundColor: "#e6eeff",
		}
		return (
			<div>
				<div style={patientListStyle}>
					Patient Statuses
					<div style={{display: 'flex', flexWrap: 'wrap', flexDirection: 'row', padding: 8}}>
						{
							sampleData.patients.map(this.generatePatientCard)
						}
					</div>
				</div>
			</div>
		)
	}
}