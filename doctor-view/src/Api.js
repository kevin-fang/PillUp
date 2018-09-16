import axios from 'axios'
let config = require('./config.json')

// get patient list
export const GetPatients = async () => {
	let request = config.ip + "/patient/all"
	console.log(request)
	try {
		let response = await axios.get(request)
		return response.data
	} catch (err) {
		throw err
	}
}

// add a new medicine
export const PostMedicine = async (id, medicine) => {
	let request = `${config.ip}/patient/${id}/medicine`
	try {
		let response = await axios.post(request, medicine)
		return response
	} catch (err) {
		throw err
	}
}

// delete a medicine
export const DeleteMedicine = async (id, medicine) => {
	let request = `${config.ip}/patient/${id}/medicine/${medicine.id}`
	try {
		let response = await axios.delete(request, medicine)
		return response
	} catch (err) {
		throw err
	}
}

// add patient
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

export const Refill = async (patientId, medicineId, count) => {
	let request = `${config.ip}/patient/${patientId}/medicine/${medicineId}/refill`
	try {
		let response = await axios.post(request, {count: count})
		return response
	} catch (err) {
		throw err
	}
}

export const AddPatient = async (patientInfo) => {
	let request = `${config.ip}/patient`
	alert(JSON.stringify(patientInfo))
	try {
		let response = await axios.post(request, patientInfo)
		return response
	} catch (err) {
		throw err
	}
}