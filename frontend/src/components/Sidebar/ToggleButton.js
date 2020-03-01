import React from 'react'
import './ToggleButton.css'
const ToggleButton = (props)=>(
		<button className="toggle_button" onClick={props.click}>
				<i className="toggle_button_line"/>
				<i className="toggle_button_line"/>
				<i className="toggle_button_line"/>
		</button>
)

export default ToggleButton
