import React from 'react'
import SettingsIcon from '@material-ui/icons/Settings';

import './Navbar.css'
import ToggleButton from '../Sidebar/ToggleButton'
import logo from '../../images/subisu_logo.png'

const Navbar = (props)=>(
		<header className="navbar border-bottom shadow-sm">
				<nav className="navbar_nav">
						<ToggleButton click={props.sideBarClickHandler}/>
						<div id="brand"> 
								<a href="/">
										<img src={logo} alt="logo"/>
								</a>
						</div>
						<div className="spacer"/>
						<div className="navbar_container">
								<div className="dropdown">
										<SettingsIcon  color="primary" className="settingButton" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"/>
										<div className="dropdown-menu dropdown-menu-right" aria-labelledby="dropdownMenuButton">
												<a className="dropdown-item" href="home">Action</a>
												<a className="dropdown-item" href="home">Change Password</a>
												<a className="dropdown-item" href="home">Logout</a>
										</div>
								</div>
						</div>
				</nav>
		</header>
)

export default Navbar
