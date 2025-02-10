let numOfRatings = 0;
function checkRating(){
    let rating = document.getElementById("rating").value;
    let result = rating * 1;
    let message = "";
    if(result > 0 && result <= 4){
        message = "My sincere apologies for not proving you the adequate services, I promise to do better!";
        numOfRatings++; 
    }else if(result > 4 && result <= 7){
        message = "I glad that you feel neutral about my expense tracker. Cool updates will be coming soon!";
        numOfRatings++; 
    }else if(result > 8 && result <= 10){
        message = "It's a pleasure to know that you find this expense tracker life changing. Thank you!";
        numOfRatings++; 
    }else{
        message = "Invalid number";
    }  
    console.log(message);
    alert(message);
    document.getElementById("numOfRatings").textContent = numOfRatings;
}