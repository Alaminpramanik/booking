$("#forward").click(function(){
    subject= $(".subject").val();
    username= $(".username").val();
    email= $(".email").val();
    number= $(".number").val();
    pickup= $(".pickup").val();
    message= $(".message").val();

    console.log('ffff',subject)
    
    // let forward_data = { 
    //     'subject':subject,
    //     'username': username,
    //     'email':email,
    //     'number': number,
    //     'pickup':pickup,
    //     'message': message,
    //   }
    //   console.log(forward_data)
    // //   SendAjax(forward_data);

});

const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
function SendAjax(forward_data){
    
  $.ajax({
    url: 'http://127.0.0.1:8000/' + id,
    method: 'GET',
    headers:{ 'X-CSRFToken': csrftoken },
    dataType: "json",
    data: forward_data,
    cached: true,
    success: function(data){
        // let load_url = 'http://127.0.0.1:8000/' + name;
        // window.location.replace(load_url);
      
    },
   
  })
}



// const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
// function forward(id){

// 	let url = 'http://127.0.0.1:8000/list/' + id +'/'
// 	$.ajax({
// 		url: url,
// 		method: 'POST',
// 		headers: {
// 		  'X-CSRFToken': csrftoken
// 		},
// 		dataType: "json",
// 		success: function(data) {
//             console.log(data)
// 			let load_url = 'http://127.0.0.1:8000/adminview/' + id 
//             window.location.replace(load_url);	
// 		},
// 	  })
// }