import {EventEmitter} from "events";
import 'whatwg-fetch'
import dispatcher from '../Dispatchers/dispatcher'
class SessionManager extends EventEmitter {
    constructor() {
        super();
        this.current_user = JSON.parse(localStorage.getItem('jtk'));
        this.logged_in = this.current_user !== null ;
        this.fetched_user = ""
    }
    getCurrentUser(){
        return this.current_user
    }
    isLogedIn(){
        return this.logged_in
    }
    setUser(object){
        console.log("Checking");
        this.current_user = object;
        this.emit("change")
    }
    LogIn(email, password){
        let the_body = {
            "email":email,
            "password":password
        };
        console.log(email);
        console.log(password);
        fetch('/ajax-login',{
            method:'POST',
            headers:{
                "Content-Type":'application/json'
            },
            body:JSON.stringify(the_body)
        }).then((response)=>{
           return response.json()
        }).then((Json)=>{
            if(Json.status === "SUCCESS"){
                alert("Login successful");
                this.current_user = Json;
                this.logged_in = true;
                localStorage.setItem('jtk', JSON.stringify(Json));
                this.emit("change");
            }else{
                alert("wrong credentials");
            }
        });
    }
    LogOut(){
        localStorage.removeItem('jtk');
        this.current_user = null;
        this.logged_in = false;
        this.emit("change")
    }

    GetFetchedUser(){
        return this.fetched_user;
    }

    LoadingUser() {
        this.fetched_user={
            fullname:"Loading",
            email:"Loading",
            id: "Loading",
            group:"Loading",
            school:"Loading"
        };
        this.emit("change")
    }
    ReturnUser(User){
        this.fetched_user = User;
        this.emit("change");
        console.log("Inside the store")
        console.log(this.fetched_user);
    }
    handleAction(action){
        switch(action.type){
            case "LOGIN" :
                this.LogIn(action.email, action.password);
                break;
            case "LOGOUT":
                this.LogOut();
                break;
            case "FETCHING_USER":
                this.LoadingUser();
                break;
            case "RETURN_USER":
                this.ReturnUser(action.user);
                break;
        }
    }
}

const sessionManager = new SessionManager;
dispatcher.register(sessionManager.handleAction.bind(sessionManager));
export default sessionManager