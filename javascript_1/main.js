let numOfRatings = 0;
function checkRating(){
    let rating = document.getElementById("rating").value;
    let message = "";
    if(rating > 0 && rating <= 4){
        message = "My sincere apologies for not proving you the adequate services, I promise to do better!";
        numOfRatings++; 
    }else if(rating > 4 && rating <= 7){
        message = "I glad that you feel neutral about my expense tracker. Cool updates will be coming soon!";
        numOfRatings++; 
    }else if(rating > 8 && rating <= 10){
        message = "It's a pleasure to know that you find this expense tracker life changing. Thank you!";
        numOfRatings++; 
    }else{
        message = "Invalid number";
    }  
    console.log(message);
    alert(message);
    document.getElementById("numOfRatings").textContent = numOfRatings;
}