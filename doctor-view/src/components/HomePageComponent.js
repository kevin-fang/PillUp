import React from 'react'

import Typography from '@material-ui/core/Typography'

// list imports
import ListItem from '@material-ui/core/ListItem'
import ListItemIcon from '@material-ui/core/ListItemIcon'
import ListItemText from '@material-ui/core/ListItemText'

// card imports
import Card from '@material-ui/core/Card'
import CardActionArea from '@material-ui/core/CardActionArea'
import CardActions from '@material-ui/core/CardActions'
import CardContent from '@material-ui/core/CardContent'
import CardMedia from '@material-ui/core/CardMedia'
import Button from '@material-ui/core/Button'
import TextField from '@material-ui/core/TextField'

// dialog imports
import Dialog from '@material-ui/core/Dialog'
import DialogActions from '@material-ui/core/DialogActions'
import DialogContent from '@material-ui/core/DialogContent'
import DialogContentText from '@material-ui/core/DialogContentText'
import DialogTitle from '@material-ui/core/DialogTitle'
import Slide from '@material-ui/core/Slide'

import { GetPatients } from '../Api.js'

let sampleData = require('../patients.json')
sampleData.patients.sort((a, b) => {
	return a.last > b.last
})

function Transition(props) {
  return <Slide direction="up" {...props} />
}

export class HomePageComponent extends React.Component {
	constructor(props) {
		super(props)
		this.state = {
			contactMessage: ""
		}
	}

	componentWillMount(props) {
		//data = await GetPatients()
		//console.log(data)
	}
	
	// generate a patient card for the main screen
	generatePatientCard = (patient) => {
		return (
			<Card key={patient.key} style={{margin: 10, width: 280, minHeight: 300}}>
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
						<Typography component="p" style={{whiteSpace: 'unset'}}>
							<b>Medications:</b> {patient.prescriptions.map(presc => presc.name).join(", ")}
						</Typography>
					</CardContent>
					<CardActions style={{justifyContent: 'center', display: 'flex', alignSelf: 'flex-end'}}>
						<Button onClick={(e) => {this.setState({[patient.key]: true})}} 
							size="small" 
							color="primary">
						  Patient Info
						</Button>
						<Button onClick={(e) => {this.setState({[patient.key + 'contact']: true})}} 
							size="small" 
							color="secondary">
						  Contact Patient
						</Button>
					</CardActions>
				</div>
			</Card>
		)
	}

	// generate a prescription card for the patient dialog
	generatePrescription = (prescription) => {
		return (
			<Card style={{margin: 10, minWidth: 250, padding: 0}}>
				<CardContent style={{}}>
					<div style={{}}>
						{prescription.name} | {prescription.dosage} | {prescription.interval} | {prescription.time}
					</div>
				</CardContent>
				<CardActions>
					<Button size='small' onClick={() => {alert('Modify Placeholder')}} style={{}}>Modify</Button>
				</CardActions>
			</Card>
		)
	}

	// generate a patient dialog
	generateDialog = (patient) => {
		return (
			<div
				key={patient.key}
				>
				<Dialog
					open={this.state[patient.key] ? true : false}
					TransitionComponent={Transition}
					contentstyle={{minWidth: 1000, justifyContent: 'center'}}
					onClose={() => {this.setState({[patient.key]: false})}}
					>
					<CardMedia
						style={{minWidth: 300, height: 400}}
						image={patient.image}
						title={patient.first + " " + patient.last}
						/>
					<DialogTitle>
						{patient.first + " " + patient.last}
					</DialogTitle>
					<DialogContent>
						<DialogContentText>
							Prescriptions:
							{patient.prescriptions.map(this.generatePrescription)}
						</DialogContentText>
					</DialogContent>
					<Button color='primary' onClick={() => this.setState({[patient.key]: false})}>
						Close
					</Button>
				</Dialog>
			</div>
		)
	}

	// generate a dialog for contacting the user
	generateContactDialog = (patient) => {
		return (
			<div
				key={patient.key + "contact"}
				>
				<Dialog
					open={this.state[patient.key + 'contact'] ? true : false}
					TransitionComponent={Transition}
					contentstyle={{minWidth: 1000, justifyContent: 'center'}}
					onClose={() => {this.setState({[patient.key + 'contact']: false})}}
					>
					<CardMedia
						style={{minWidth: 300, height: 400}}
						image={patient.image}
						title={patient.first + " " + patient.last}
						/>
					<DialogTitle>
						{patient.first + " " + patient.last}
					</DialogTitle>
					<DialogContent>
						<TextField
							style={{width: "100%"}}
							id="message"
							label="Type message here"
							onChange={(e) => {
								this.setState({
									contactMessage: e.target.value
								})
							}}
							multiline
						/>
					</DialogContent>
					<Button onClick={(e) => {
						console.log(this.state.contactMessage)
						this.setState({[patient.key + 'contact']: false})
					}}>
						Submit
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
				{	
					sampleData.patients.map(this.generateContactDialog)
				}
			</div>
		)
	}
}