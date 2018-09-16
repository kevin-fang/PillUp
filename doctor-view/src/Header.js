import React from 'react'
import { Link } from 'react-router-dom'

// @material-ui/core imports
import SwipeableDrawer from '@material-ui/core/SwipeableDrawer'
import Toolbar from '@material-ui/core/Toolbar'
import AppBar from '@material-ui/core/AppBar'
import Typography from '@material-ui/core/Typography'
import List from '@material-ui/core/List'
import Divider from '@material-ui/core/Divider'
import IconButton from '@material-ui/core/IconButton'
import MenuItem from '@material-ui/core/MenuItem'
import SvgIcon from '@material-ui/core/SvgIcon'
import Button from '@material-ui/core/Button'

// list imports
import ListItem from '@material-ui/core/ListItem'
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';

// menu imports
import HomeOutlineIcon from '@material-ui/icons/HomeOutlined'
import MenuOutlineIcon from '@material-ui/icons/MenuOutlined'
import PermIdentityOutlineIcon from '@material-ui/icons/PermIdentityOutlined'
import InfoOutlineIcon from '@material-ui/icons/InfoOutlined'
import DoneOutlineIcon from '@material-ui/icons/DoneOutlined'

// card imports
import Card from '@material-ui/core/Card';
import CardActionArea from '@material-ui/core/CardActionArea';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';

// generate a home SVG icon
function HomeIcon(props) {
	return (
			<SvgIcon {...props}>
				<path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z" />
			</SvgIcon>
		)
}

// disable underline for navigation bar
const noLinkUnderline = { 
    textDecoration: 'none' 
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
		// create the side list containing home, patient, about, and sign out buttons
		const sideList = (
			<div style={{width: "100%"}}>
				<Link to='/' style={noLinkUnderline}>
					<ListItem button>
						<ListItemIcon>
							<HomeOutlineIcon />
						</ListItemIcon>
						<ListItemText primary="Home" />
					</ListItem>
				</Link>
				{/*
				<Link to='/patient' style={noLinkUnderline}>
					<ListItem button>
						<ListItemIcon>
							<PermIdentityOutlineIcon />
						</ListItemIcon>
						<ListItemText primary="Patient" />
					</ListItem>
				</Link>
				*/}	
				<Link to='/about' style={noLinkUnderline}>
					<ListItem button>
						<ListItemIcon>
							<InfoOutlineIcon />
						</ListItemIcon>
						<ListItemText primary="About" />
					</ListItem>
				</Link>
				<Divider />
				<ListItem button>
					<ListItemIcon>
						<DoneOutlineIcon />
					</ListItemIcon>
					<ListItemText primary="Sign out" />
				</ListItem>
			</div>
		)

		// create main doctor card
		const doctorCard = (
			<Card style={{margin: 10}}>
				<CardMedia
					style={{height: 250, objectFit: 'cover'}}
					image="https://images.pexels.com/photos/415829/pexels-photo-415829.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260"
					title="Shayan"
				/>
				<CardContent style={{padding: 20, minWidth: 275}}>
					{/*<Typography className={{marginBottom: 16, fontSize: 14}} color="textSecondary">
						Welcome
					</Typography>*/}
					<Typography gutterBottom variant="headline" component="h2">
						Welcome, Doctor Sun
					</Typography>
					<Typography component="p">
						Johns Hopkins Hospital
					</Typography>
				</CardContent>
			</Card>
		)

		return (
			<div>
				{/* Create material design app bar */}
				<AppBar>
					<Toolbar>
						<IconButton color="inherit" 
							aria-label="Menu" 
							onClick={this.openNavigationMenu}
							style={{marginLeft: -12, marginRight: 20}}>
							<MenuOutlineIcon />
						</IconButton>
						<Typography variant="title" color="inherit">
							PillUp	
						</Typography>
					</Toolbar>
				</AppBar>
				<SwipeableDrawer
					open={this.state.open}
					onOpen={this.openNavigationMenu}
					onClose={this.closeNavigationMenu}>
					<div
						tabIndex=''
						onClick={this.closeNavigationMenu}
						role='button'
						style={{marginTop: 10}}
						onKeyDown={this.closeNavigationMenu}
						>
						{doctorCard}
						<div style={{marginTop: 10, width: "100%"}}>
							{sideList}
						</div>
					</div>
				</SwipeableDrawer>
			</div>
		)
	}
}