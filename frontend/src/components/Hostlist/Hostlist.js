import React,{Component} from 'react';

import axios from 'axios';

export default class Hostlist extends Component{
		state = {
				hostlist:[]
		};

		componentDidMount(){
				this.getTodo();
		}

		getTodo(){
				axios
						.get('/api/v1/')
						.then(res => {
								this.setState({hostlist:res.data})
						})
						.catch(err=>
								console.log(err)
						)}

		render(){
				return (
						<div>
								{this.state.hostlist.map(host=>(
										<div key={host.id}>
												<h1>{host.hostname}</h1>
												<p>{host.vendor}</p>
										</div>
								))}
						</div>
				)
		}
}
