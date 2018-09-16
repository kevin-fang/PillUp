import axios from 'axios'
let config = require('./config.json')

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

export const PostMedicine = async (id, medicine) => {
	let request = `${config.ip}/patient/${id}/medicine`
	try {
		let response = await axios.post(request, medicine)
		return response
	} catch (err) {
		throw err
	}
}

export const DeleteMedicine = async (id, medicine) => {
	let request = `${config.ip}/patient/${id}/medicine/${medicine.id}`
	try {
		let response = await axios.delete(request, medicine)
		return response
	} catch (err) {
		throw err
	}
}