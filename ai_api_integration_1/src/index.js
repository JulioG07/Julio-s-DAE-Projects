import { initializeApp } from "firebase/app";
import { getFirestore, collection, addDoc, onSnapshot, query, orderBy, serverTimestamp, doc, getDoc, setDoc, where } from "firebase/firestore";
import { getAuth, createUserWithEmailAndPassword, signOut, signInWithEmailAndPassword, onAuthStateChanged } from "firebase/auth";

console.log('JavaScript file loaded');
const firebaseConfig = {
    apiKey: "AIzaSyAIQp_M0LiPkucvamm6Dd8mbl_TjzOc-JM",
    authDomain: "expense-tracker-v1-6483a.firebaseapp.com",
    projectId: "expense-tracker-v1-6483a",
    storageBucket: "expense-tracker-v1-6483a.firebasestorage.app",
    messagingSenderId: "1058102450247",
    appId: "1:1058102450247:web:1c417efcdff225f7a63962"
}

//init firebase app
initializeApp(firebaseConfig);

//init services
const db = getFirestore()
const auth = getAuth()

//init references
const colRef = collection(db, 'users')
const q = query(colRef, orderBy('createdAt'))

//real time data collection
onSnapshot(q, (snapshot) => {
    let users = []
    snapshot.forEach(doc => {
        users.push({ ...doc.data(), id: doc.id })
        });
    console.log(users)
})

document.addEventListener('DOMContentLoaded', () => {
    //siging up users 
    const signupForm = document.querySelector('.signup')
    if (signupForm) {
        signupForm.addEventListener('submit', (e) => {
            e.preventDefault()
            const email = signupForm.email.value
            const password = signupForm.password.value
            const firstName = signupForm.firstName.value
            const lastName = signupForm.lastName.value

            createUserWithEmailAndPassword(auth, email, password)
                .then((cred) => {
                    console.log('user created:', cred.user)
                    // Add user information to Firestore Database
                    return setDoc(doc(db, 'users', cred.user.uid), { 
                        Fname: firstName,
                        Lname: lastName,
                        Email: email,
                        createdAt: serverTimestamp(),
                        userId: cred.user.uid
                    });
                })
                .then(() => {
                    signupForm.reset()
                    //console.log('User information added to Firestore')
                    window.location.href = 'home.html';
                })
                .catch((err) => {
                    console.log(err.message)
                })
        })
    }

    //login and login out users 
    const logoutButton = document.querySelector('.logout')
    if (logoutButton) {
        logoutButton.addEventListener('click', () => {
            signOut(auth)
                .then(() => {
                    //console.log('The user signed out')
                    window.location.href = 'login.html';
                })
                .catch((err) => {
                    console.log(err.message)
                })
        })
    }

    const loginForm = document.querySelector('.login')
    if (loginForm) {
        loginForm.addEventListener('submit', (e) => {
            e.preventDefault()
            const email = loginForm.email.value
            const password = loginForm.password.value
            signInWithEmailAndPassword(auth, email, password)
                .then((cred) => {
                    //console.log('user logged in: ', cred.user)
                    window.location.href = 'home.html';
                })
                .catch((err) => {
                    console.log(err.message)
                })
        })
    }

    function displayFirstNameByQuery(userID) {
        console.log('Searching for user with ID:', userID);
        // Create a query to find documents where userId equals the provided userID
        const q = query(collection(db, 'users'), where('userId', '==', userID));
    
        onSnapshot(q, (snapshot) => {
            if (snapshot.empty) {
                console.error('No document found with userId matching:', userID);
                return;
            }
            // We should only have one document matching the userId
            const userData = snapshot.docs[0].data();
            const firstNameElement = document.getElementById('firstName');
            if (firstNameElement) {
                firstNameElement.textContent = userData.Fname;
                console.log("User first name displayed:", userData.Fname);
            } else {
                console.error('firstName element not found in the DOM');
            }
        });
    }
    //call functions here
    onAuthStateChanged(auth, (user) => {
    if (user) {
        console.log('User is logged in:', user);
        displayFirstNameByQuery(user.uid);
    } else {
        console.log('User is logged out');
    }
    })
})