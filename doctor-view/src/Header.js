import React from 'react'
import { Link } from 'react-router-dom'

// @material-ui/core stuff
import Drawer from '@material-ui/core/Drawer'
import Toolbar from '@material-ui/core/Toolbar'
import AppBar from '@material-ui/core/AppBar'
import Typography from '@material-ui/core/Typography'
import List from '@material-ui/core/List'
import Divider from '@material-ui/core/Divider';

// list stuff
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';

// menu stuff
import IconButton from '@material-ui/core/IconButton'
import MenuItem from '@material-ui/core/MenuItem'
import MenuIcon from '@material-ui/icons/Menu'
import SvgIcon from '@material-ui/core/SvgIcon'
import AccessibilityIcon from '@material-ui/icons/Accessibility'
import InfoIcon from '@material-ui/icons/Info'


function HomeIcon(props) {
	return (
			<SvgIcon {...props}>
				<path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z" />
			</SvgIcon>
		)
}

export default class Header extends React.Component {

	constructor(props) {
		// set up constructors and navigation
		super(props)
		this.state = {
			open: false,
		}
		this.openNavigationMenu = this.openNavigationMenu.bind(this)
		this.closeNavigationMenu = this.closeNavigationMenu.bind(this)
	}

	// set up basic functions for opening/closing navigation menu
	openNavigationMenu() {
		this.setState({open: true})
	}

	closeNavigationMenu() {
		this.setState({open: false})
	}

	render () {

		const sideList = (
			<div style={{width: 250}}>
				<ListItem button onClick={() => alert('test')}>
					<ListItemIcon>
						<HomeIcon />
					</ListItemIcon>
					<ListItemText primary="Home" />
				</ListItem>
				<ListItem button>
					<ListItemIcon>
						<AccessibilityIcon />
					</ListItemIcon>
					<ListItemText primary="Patient" />
				</ListItem>
				<ListItem button>
					<ListItemIcon>
						<InfoIcon />
					</ListItemIcon>
					<ListItemText primary="About" />
				</ListItem>
			</div>
		)

		return (
			<div>
				<AppBar
					onLeftIconButtonTouchTap={() => alert('test')}>
					<Toolbar>
						<IconButton color="inherit" 
							aria-label="Menu" 
							onClick={this.openNavigationMenu}
							style={{marginLeft: -12, marginRight: 20}}>
							<MenuIcon />
						</IconButton>
						<Typography variant="title" color="inherit">
							PillUp	
						</Typography>
					</Toolbar>
				</AppBar>
				<Drawer
					open={this.state.open}
					onClose={this.closeNavigationMenu}>
					<div
						tabIndex=''
						onClick={this.closeNavigationMenu}
						role='button'
						style={{marginTop: 10}}
						onKeyDown={this.closeNavigationMenu}
						>
						{sideList}
					</div>
				</Drawer>
			</div>
		)
	}
}