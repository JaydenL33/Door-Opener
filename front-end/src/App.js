
import React, { Component } from 'react';

import "./App.css";
import HomeScreen from './Pages/HomeScreen';
import {
	BrowserRouter as Router,
	Switch,
	Route,
  } 
from "react-router-dom";



// a in style.css has now become <link> so remember to replace that in the CSS. 

class App extends Component {
    
    render() {
        return (
            <Router>
                <Switch>
                    <Route path="/">
                      <HomeScreen/>
                     </Route>
                    <Route path="/Indicators">
                      <h1>Test</h1>
                    </Route>
                    <Route path="/AboutUs">
                      <h1>Test</h1>
                    </Route>
                    <Route path="/ContactUs">
                      <h1>Test</h1>
                    </Route>
                </Switch>
            </Router>
        )
    }
};



export default App;