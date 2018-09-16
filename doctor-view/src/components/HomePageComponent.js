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

import AddCircleOutlineIcon from '@material-ui/icons/AddCircleOutlined'

// dialog imports
import Dialog from '@material-ui/core/Dialog'
import DialogActions from '@material-ui/core/DialogActions'
import DialogContent from '@material-ui/core/DialogContent'
import DialogContentText from '@material-ui/core/DialogContentText'
import DialogTitle from '@material-ui/core/DialogTitle'
import Slide from '@material-ui/core/Slide'

import { GetPatients, PostMedicine, DeleteMedicine, AddPatient } from '../Api.js'

let sampleData = require('../patients.json')
sampleData.patients.sort((a, b) => {
	return a.last > b.last
})

function Transition(props) {
	return <Slide direction="up" {...props} />
}

function GetKey(patient, id) {
	return `${patient.id}/${id}`
}

function FormatPhone(phone) {

	return `(${phone.slice(0, 3)})-${phone.slice(3, 6)}-${phone.slice(6, 10)}`
}

let keys = {
	ADD_MEDICINE: 'add_medicine',
	PATIENT: 'patient', 
	CONTACT: 'contact',
	DIALOG: 'dialog',
	MEDICINE_NAME: 'medicine_name',
	MEDICINE_DESCRIPTION: "medicine_desc",
	MEDICINE_SIDE_EFFECTS: "medicine_side_eff",
	MEDICINE_INTERVAL: "every",
	MEDICINE_CARTRIDGE_NO: "cartridge",
	MEDICINE_COUNT: "count"
}

export class HomePageComponent extends React.Component {
	constructor(props) {
		super(props)
		this.state = {
			contactMessage: "",
			patientsLoaded: false,
			newUser: {}
		}
	}

	async componentWillMount(props) {
		let data = await GetPatients()
		this.patients = data
		this.setState({
			patientsLoaded: true
		})
	}

	async refresh() {
		let data = await GetPatients()
		this.patients = data
		this.setState({
			patientsLoaded: true
		})
	}
	
	// generate a patient card for the main screen
	generatePatientCard = (patient) => {
		return (
			<Card key={GetKey(patient, keys.PATIENT)} style={{margin: 10, width: 280, minHeight: 300}}>
				<div style={{}}>
					{/*<Typography className={{marginBottom: 16, fontSize: 14}} color="textSecondary">
						Welcome
					</Typography>*/}
					<CardMedia
						style={{height: 250, objectFit: 'cover'}}
						image={patient.profile_pic}
						title={patient.first_name}
						/>
					<CardContent>
						<Typography gutterBottom variant="headline" component="h2">
							{patient.last_name + ", " + patient.first_name}
						</Typography>
						<Typography component="p">
							<b>Email:</b> {patient.email}
						</Typography>
						<Typography component="p">
							<b>Phone:</b> {FormatPhone(patient.phone)}
						</Typography>
						<Typography component="p" style={{whiteSpace: 'unset'}}>
							<b>Medications:</b> {patient.medicine.map(presc => presc.name).join(", ")}
						</Typography>
					</CardContent>
					<CardActions style={{justifyContent: 'center', display: 'flex', alignSelf: 'flex-end'}}>
						<Button onClick={(e) => {this.setState({[patient.id]: true})}} 
							size="small" 
							color="primary">
						  Patient Info
						</Button>
						<Button onClick={(e) => {this.setState({[GetKey(patient, keys.CONTACT)]: true})}} 
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
	generatePrescription = (patient, prescription) => {
		var d = new Date(0)
		d.setUTCSeconds(prescription.last_dispense)

		return (
			<Card key={prescription.id} style={{margin: 10, minWidth: 250, padding: 0}}>
				<CardContent style={{}}>
					<div style={{}}>
						{prescription.name} | {prescription.count} pill(s) left | {prescription.description} | Last dispensed: {d.toString()}
					</div>
				</CardContent>
				<CardActions>
					<Button size='small' 
						onClick={async () => {
							try {
								console.log(prescription.id)
								console.log(patient)
								let response = await DeleteMedicine(patient.id, prescription)
								this.setState({
									[patient.id]: true
								}, () => {
									this.refresh()
								})
							} catch (err) {
								console.log(err)
								alert(err)
							}
						}} 
						style={{}}>Delete</Button>
				</CardActions>
			</Card>
		)
	}

	// generate a dialog to add medicine to patients
	generateMedicineDialog = (patient) => {
		return (
			<div key={GetKey(patient, keys.ADD_MEDICINE)}>
				<Dialog
					open={this.state[GetKey(patient, keys.ADD_MEDICINE)] ? true : false}
					TransitionComponent={Transition}
					onClose={() => {this.setState(
						{
						[GetKey(patient, keys.ADD_MEDICINE)]: false}
						)}}>
					<Card key={GetKey(patient, keys.MEDICINE_NAME)} style={{margin: 10, minWidth: 250, minHeight: 450, padding: 0}}>
						<CardContent style={{}}>
							Add New Medication
							<TextField
								style={{width: "100%", marginTop: 10}}
								label="Medication Name"
								onChange={(e) => {
									this.setState({
										[GetKey(patient, keys.MEDICINE_NAME)]: e.target.value
									})
								}}
							/>
							<TextField
								style={{width: "100%", marginTop: 10}}
								label="Brief Description"
								onChange={(e) => {
									this.setState({
										[GetKey(patient, keys.MEDICINE_DESCRIPTION)]: e.target.value
									})
								}}
							/>
							<TextField
								style={{width: "100%", marginTop: 10}}
								label="Side Effects"
								onChange={(e) => {
									this.setState({
										[GetKey(patient, keys.MEDICINE_SIDE_EFFECTS)]: e.target.value
									})
								}}
							/>
							<TextField
								style={{width: "100%", marginTop: 10}}
								label="Interval (seconds)"
								onChange={(e) => {
									this.setState({
										[GetKey(patient, keys.MEDICINE_INTERVAL)]: e.target.value
									})
								}}
							/>
							<TextField
								style={{width: "100%", marginTop: 10}}
								label="Cartridge #"
								onChange={(e) => {
									this.setState({
										[GetKey(patient, keys.MEDICINE_CARTRIDGE_NO)]: e.target.value
									})
								}}
							/>
							<TextField
								style={{width: "100%", marginTop: 10}}
								label="# of total pills"
								onChange={(e) => {
									this.setState({
										[GetKey(patient, keys.MEDICINE_COUNT)]: e.target.value
									})
								}}
							/>
						</CardContent>
						<CardActions>
							<Button size='small' onClick={async () => {
								let medicine = {
									name: this.state[GetKey(patient, keys.MEDICINE_NAME)],
									description: this.state[GetKey(patient, keys.MEDICINE_DESCRIPTION)],
									side_effects: this.state[GetKey(patient, keys.MEDICINE_SIDE_EFFECTS)],
									every: this.state[GetKey(patient, keys.MEDICINE_INTERVAL)],
									cartridge: this.state[GetKey(patient, keys.MEDICINE_CARTRIDGE_NO)],
									count: this.state[GetKey(patient, keys.MEDICINE_COUNT)]
								}
								if (!(medicine.name && medicine.description && medicine.side_effects && medicine.every && medicine.cartridge && medicine.count)) {
									alert("All fields must be full before submitting medicine.")
								} else {
									try {
										let result = await PostMedicine(patient.id, medicine)
										this.setState({
											[GetKey(patient, keys.ADD_MEDICINE)]: false
										}, () => {
											this.refresh()
										})
									} catch (err) {
										alert(err)
									}
								}
							}} style={{}}>Add</Button>
						</CardActions>
					</Card>
				</Dialog>
			</div>
		)
	}

	// generate a patient dialog
	generateDialog = (patient) => {
		return (
			<div
				key={GetKey(patient, keys.DIALOG)}
				>
				<Dialog
					open={this.state[patient.id] ? true : false}
					TransitionComponent={Transition}
					contentstyle={{minWidth: 1000, justifyContent: 'center'}}
					onClose={() => {this.setState({[patient.key]: false})}}
					>
					<CardMedia
						style={{minWidth: 300, height: 400}}
						image={patient.profile_pic}
						title={patient.first_name + " " + patient.last_name}
						/>
					<DialogTitle>
						{patient.first_name + " " + patient.last_name}
					</DialogTitle>
					<DialogContent>
						<DialogContentText>
							{patient.medicine.map(medicine => this.generatePrescription(patient, medicine))}
						</DialogContentText>
					</DialogContent>
					<Button color='primary' onClick={() => this.setState({[GetKey(patient, keys.ADD_MEDICINE)]: true})}>
						Add Medicine
					</Button>
					<Button color='primary' onClick={() => this.setState({[patient.id]: false})}>
						Dismiss
					</Button>
				</Dialog>
			</div>
		)
	}

	// generate a dialog for contacting the user
	generateContactDialog = (patient) => {
		return (
			<div
				key={GetKey(patient, keys.CONTACT)}
				>
				<Dialog
					open={this.state[GetKey(patient, keys.CONTACT)] ? true : false}
					TransitionComponent={Transition}
					contentstyle={{minWidth: 1000, justifyContent: 'center'}}
					onClose={() => {this.setState({[GetKey(patient, keys.CONTACT)]: false})}}
					>
					<CardMedia
						style={{minWidth: 300, height: 400}}
						image={patient.profile_pic}
						title={patient.first_name + " " + patient.last_name}
						/>
					<DialogTitle>
						{patient.first_name + " " + patient.last_name}
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
						this.setState({[GetKey(patient, keys.CONTACT)]: false})
					}}>
						Submit
					</Button>
					<Button color='secondary' 
						onClick={(e) => {
						this.setState({[GetKey(patient, keys.CONTACT)]: false})
					}}>
						Cancel
					</Button>
				</Dialog>
			</div>
		)
	}

/*
	{
	    "first_name": "string",
	    "last_name": "string",
	    "doctor_id": "string",
	    "address": "string",
	    "email": "string",
	    "phone": "string",
	    "profile_pic": "url",
	}
*/
	newPatientDialog = () => {
		return (
			<Dialog
				open={this.state.addPatient}
				TransitionComponent={Transition}
				contentstyle={{minWidth: 1000, justifyContent: 'center'}}
				onClose={() => this.setState({addPatient: false})}
				>
				<DialogTitle>
					New Patient
				</DialogTitle>
				<DialogContent>
					<TextField
						style={{width: "100%"}}
						label="First Name"
						onChange={(e) => {
							const newUser = this.state.newUser
							newUser.first_name = e.target.value
							this.setState({
								newUser,
							})
						}}
					/>
					<TextField
						style={{width: "100%"}}
						label="Last Name"
						onChange={(e) => {
							const newUser = this.state.newUser
							newUser.last_name = e.target.value
							this.setState({
								newUser,
							})
						}}
					/>
					<TextField
						style={{width: "100%"}}
						label="Doctor ID"
						onChange={(e) => {
							const newUser = this.state.newUser
							newUser.doctor_id = e.target.value
							this.setState({
								newUser,
							})
						}}
					/>
					<TextField
						style={{width: "100%"}}
						label="Address"
						onChange={(e) => {
							const newUser = this.state.newUser
							newUser.address = e.target.value
							this.setState({
								newUser,
							})
						}}
					/>
					<TextField
						style={{width: "100%"}}
						label="Email"
						onChange={(e) => {
							const newUser = this.state.newUser
							newUser.email = e.target.value
							this.setState({
								newUser,
							})
						}}
					/>
					<TextField
						style={{width: "100%"}}
						label="Phone"
						onChange={(e) => {
							const newUser = this.state.newUser
							newUser.phone = e.target.value
							this.setState({
								newUser,
							})
						}}
					/>

					<TextField
						style={{width: "100%"}}
						label="Profile Picture (URL)"
						onChange={(e) => {
							const newUser = this.state.newUser
							newUser.profile_pic = e.target.value
							this.setState({
								newUser,
							})
						}}
					/>
				</DialogContent>
				<Button color='primary' onClick={async (e) => {
					try {
						let response = await AddPatient(this.state.newUser)
						this.setState({addPatient: false})
					} catch (err) {
						alert(err)
					}
				}}>
					Submit
				</Button>
				<Button color='secondary' 
					onClick={(e) => {
						this.setState({addPatient: false})
				}}>
					Cancel
				</Button>
			</Dialog>
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
		if (this.state.patientsLoaded) {
			return (
				<div>
					<div style={patientListStyle}>
						Patient Statuses
						<div style={{display: 'flex', flexWrap: 'wrap', justifyContent: 'center', flexDirection: 'row', padding: 8}}>
							{
								this.patients.map(this.generatePatientCard)
							}
						</div>
					</div> 

					{	
						this.patients.map(this.generateDialog)
					}
					{	
						this.patients.map(this.generateContactDialog)
					}
					{
						this.patients.map(this.generateMedicineDialog)
					}
					{
						this.newPatientDialog()
					}
					<Button variant='extendedFab' color='secondary' style={{position: 'fixed', bottom: 20, right: 20}} onClick={() => {
						this.setState({
							addPatient: true
						})
					}}>
						<AddCircleOutlineIcon style={{marginRight: 5, marginTop: 4}} />
						Patient
					</Button>
				</div>
			)
		} else {
			return (
				<div style={{paddingTop: 80, paddingLeft: 10}}>
					Loading...
				</div>
			)
		}
	}
}