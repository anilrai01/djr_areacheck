import React from 'react';
import {Link} from 'react-router-dom'

import List from '@material-ui/core/List'
import ListItem from '@material-ui/core/ListItem'
import ListItemText from '@material-ui/core/ListItemText'

const SidebarItem = ({show,label,items,to,depthStep=10,depth=0,...rest}) =>{
		return (
				<>
				<Link to={to}>
				<ListItem button dense {...rest}>
				<ListItemText style={{paddingLeft: depth * depthStep}}>
				{label}
				</ListItemText>
				</ListItem>
				</Link>
				{Array.isArray(items) && show?(
						<List disablePadding dense className="sub_menu">
						{items.map( subItem =>(
								<SidebarItem 
								key={subItem.name}
								depth = {depth + 1}
								depthStep = {depthStep}
								{...subItem}
								/>
						))}
						</List>
				):null}
				</>
		)
}

export default SidebarItem
