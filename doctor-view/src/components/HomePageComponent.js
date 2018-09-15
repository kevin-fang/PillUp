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

// dialog imports
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';
import Slide from '@material-ui/core/Slide';

let sampleData = require('../patients.json')
sampleData.patients.sort((a, b) => {
	return a.name > b.name
})

export class HomePageComponent extends React.Component {
	constructor(props) {
		super(props)
		this.state = {
		}
	}
	
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
						title={patient.first}
						/>
					<CardContent>
						<Typography gutterBottom variant="headline" component="h2">
							{patient.last + ", " + patient.first}
						</Typography>
						<Typography component="p">
							<b>Status:</b> {patient.status}
						</Typography>
						<Typography component="p">
							<b>Medications:</b> {patient.prescriptions.join(", ")}
						</Typography>
					</CardContent>
					<CardActions style={{position: 'relative', bottom: 0}}>
						<Button onClick={(e) => {this.setState({[patient.key]: true})}} size="small" color="primary">
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

	generateDialog = (patient) => {
		return (
			<div>
				<Dialog
					open={this.state[patient.key] ? true : false}
					contentStyle={{minWidth: 1000, justifyContent: 'center'}}
					onClose={() => {this.setState({[patient.key]: false})}}
					>
					<CardMedia
						style={{width: 500, height: 400, objectFit: 'cover'}}
						image={patient.image}
						title={patient.first + " " + patient.last}
						/>
					<DialogTitle>
						{patient.first + " " + patient.last}
					</DialogTitle>
					<Button onClick={() => this.setState({[patient.key]: false})}>
						Close
					</Button>
				</Dialog>
			</div>
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
					<div style={{display: 'flex', flexWrap: 'wrap', justifyContent: 'center', flexDirection: 'row', padding: 8}}>
						{
							sampleData.patients.map(this.generatePatientCard)
						}
					</div>
				</div> 

				{	
					sampleData.patients.map(this.generateDialog)
				}
			</div>
		)
	}
}