import { initializeApp } from "firebase/app";
import { getFirestore, collection, addDoc, onSnapshot, query, orderBy, serverTimestamp, doc, getDoc } from "firebase/firestore";
import { getAuth, createUserWithEmailAndPassword, signOut, signInWithEmailAndPassword, onAuthStateChanged } from "firebase/auth";

console.log('JavaScript file loaded'); // Add this line to check if the script is loaded

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
                    // Add user information to Firestore
                    return addDoc(colRef, {
                        Fname: firstName,
                        Lname: lastName,
                        Email: email,
                        createdAt: serverTimestamp(),
                        userId: cred.user.uid
                    })
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
    // Function to retrieve and display user first name
    function displayFirstName(userID) {
        console.log('Fetching data for userID:', userID); // Log the userID
        const userDocRef = doc(db, 'users', userID);
        getDoc(userDocRef)
            .then((doc) => {
                if (doc.exists()) {
                    const userData = doc.data();
                    document.getElementById('firstName').textContent = userData.Fname;
                } else {
                    console.log('No such document!');
                }
            })
            .catch((error) => {
                console.log('Error getting document:', error);
            });
    }
    // Listen for auth state changes
    onAuthStateChanged(auth, (user) => {
        if (user) {
            console.log('User is logged in:', user);
            displayFirstName(user.uid);
        } else {
            console.log('User is logged out');
        }
    })
})