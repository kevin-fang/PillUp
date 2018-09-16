import React, { Component } from 'react';
import Main from './Main.js'
import Header from './Header.js'

import { MuiThemeProvider, createMuiTheme } from '@material-ui/core/styles'; // v1.x

const muiTheme = createMuiTheme({

})

class App extends Component {
	

	render() {
		return (
			<div className="App">
				<MuiThemeProvider theme={muiTheme}>
					<div className='App'>
						<Header />
						<Main />
					</div>
				</MuiThemeProvider>
			</div>
		)
	}
}

export default App;
