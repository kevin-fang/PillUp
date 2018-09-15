import axios from 'axios'
let config = require('./config.json')

export const GetPatients = await (callback) => {
	let request = config.ip + ':' + config.port + "/patient/all"
	console.log(request)
	axios.get(request)
		.then(response => {
			alert("Good", response.data)
		}).catch(err => {
			alert(err)
		})
}