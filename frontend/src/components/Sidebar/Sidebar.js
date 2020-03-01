import React,{Component}from 'react';
import List from '@material-ui/core/List'
import ToggleButton from '../Sidebar/ToggleButton'

import SidebarItem from './SidebarItem.js'
import './Sidebar.css'

const items = [
		{ name:'Host', label:'Host',to:'/host/' },
		{ 
				name:'Node',
				label:'Node',
				show:false,
				items:[
						{ name:'ack_node',label:'Ack Node',to:'/'},
						{ name:'DownNode',label:'Down Node',to:'/downnodes/'},
						{ name:'AllNodes',label:'All Nodes',to:"/allnodes/"},
				]
		},
		{ 
				name:'reasons',
				label:'Reasons',
				show:false,
				items:[
						{ name:'reasons',label:'Reasons',to:"/reasons/"},
						{ name:'subReasons',label:'Sub Reasons',to:"/subreasons/"},
				]
		},
		{ name:'Users',label:'Users',to:"/users/"},
]

class Sidebar extends Component{
		constructor(props) {
				super(props);

				// This binding is necessary to make `this` work in the callback
				this.subMenuToggler = this.subMenuToggler.bind(this);
		}

		state = {
				items:items,
				depth:10,
				depthStep:0,
		}

		subMenuToggler = (event,index) =>{
				this.setState ((prevState) => {
						let clicked =this.state.items[index]
						clicked.show = !clicked.show
						if(clicked.show !==undefined){
								this.setState(() => ({
										items:[...this.state.items.slice(0,index),clicked,...this.state.items.slice(index+1)]
								}))
						}
				})
		}
		render(){
				let sidebarClasses = "sidebar"
				if(this.props.show){
						sidebarClasses = "sidebar show"
				}
				return (
						<div className={sidebarClasses}>
								<List disablePadding dense>
										<div className="btnHolder">
										<ToggleButton click={this.props.sideBarClickHandler}/>
												<span className="appName"> Areacheck</span>
										</div>
										{this.state.items.map((sidebarItem,index)=>(
												<SidebarItem 
														show={sidebarItem.show}
														onClick={(event) => this.subMenuToggler(event,index)}
														key={`${sidebarItem.name}${index}`}
														depthStep = {this.depthStep}
														depth={this.depth}
														{...sidebarItem}
												/>
										))}
								</List>
						</div>
				)
		}
}

export default Sidebar;
