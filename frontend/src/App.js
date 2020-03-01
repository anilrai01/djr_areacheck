import React,{Component} from 'react';
import {
		BrowserRouter as Router,
		Route,
		Link,
} from 'react-router-dom'


import './App.css';

import Sidebar from './components/Sidebar/Sidebar'
import Navbar from './components/Navbar/Navbar'
import HostList from './components/Hostlist/Hostlist'
import Backdrop from './components/Backdrop/Backdrop'


const routes = [
		{
				path: '/',
				exact:true,
				main: () => <h1>Ack Nodes</h1>
		},
		{
				path: '/downnodes/',
				exact:true,
				main: () => <h1>Down Nodes</h1>
		},
		{
				path: '/Host/',
				exact:true,
				main: () => <HostList/>
		},
		{
				path: '/allnodes/',
				exact:true,
				main: () => <h1>All Nodes</h1>
		},
		{
				path: '/reasons/',
				exact:true,
				main: () => <h1>Reasons</h1>
		},
		{
				path: '/subreasons/',
				exact:true,
				main: () => <h1>Sub Reasons</h1>
		},
		{
				path: '/users/',
				exact:true,
				main: () => <h1>Users</h1>
		},
]



class App extends Component{
		state = {
				showSidebar:false,
		}

		subMenuToggler = (item,index) => {
				console.log(index)
		}

		toggleSidebar = () =>{
				this.setState((prevState) => ({
						showSidebar: !prevState.showSidebar
				}))
		}

		backdropClickHandler = () =>{
				this.setState({showSidebar:false});
		}


		render(){
				let backdrop;
				if(this.state.showSidebar){
						backdrop = <Backdrop click={this.backdropClickHandler}/>
				}
				return (
						<Router>
								<div className="">
										<Sidebar show={this.state.showSidebar} sideBarClickHandler = {this.toggleSidebar}  />
										{backdrop}
										<Navbar sideBarClickHandler = {this.toggleSidebar} />
										<main className="container">
												{routes.map((route) => (
														<Route 
																key={route.path}
																path={route.path}
																exact={route.exact}
																component={route.main}
														/>
												))}
										</main>
								</div>
						</Router>
				)
		}
}

export default App;
