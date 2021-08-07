import React, { Component } from "react";
import { Card, Button } from "react-bootstrap"
import { BrowserRouter as Router, Switch, Route, Link, Redirect } from "react-router-dom";
import ContentPage from './ContentPage';

export default class HomePage extends Component {
    constructor(props) {
        super(props);
    }

    renderCard = () => {
        return (
            <Card style={{ width:'18rem' }}>
                <Card.Header>Featured</Card.Header>
                <Card.Body>
                    <Card.Title>Special title treatment</Card.Title>
                    <Card.Text>
                        With supporting text below as a natural lead-in to additional content.
                    </Card.Text>
                    <Link to='/content'>
                        <Button variant="primary">Go somewhere</Button>
                    </Link>
                </Card.Body>
            </Card>
        );
    }

    render() {
        return (
            <Router>
                <Switch>
                    <Route exact path='/' render={
                        () => {
                            return this.renderCard();
                        }
                    } />
                    <Route path='/content' component={ContentPage} />
                </Switch>
            </Router>
        );
    }
}