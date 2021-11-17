$("#approved").click(function(){
//   var EmpName = $("div#subject div#approved").attr('class');
//   console.log('dfd', EmpName)
// // Undefined check
//   if (Object.prototype.toString.call(EmpName) === '[object Undefined]'){
//     subject= $(".subject").values
//     console.log('ffff',subject)
//   }
      // sub= document.querySelector(".subject")
    // subject=document.getElementsByClassName(subject).HTMLCollection
    // document.querySelector('*');
    // subject= $(".subject").innerHTML
    // subject= $(".subject").querySelector
    subject= document.querySelector('#subject').innerText
    // username= $(".username").val();
    // email= $(".email").val();
    // number= $(".number").val();
    // pickup= $(".pickup").val();
    // message= $(".message").val();

    console.log('ffff',subject)
    
    let forward_data = { 
        'subject':subject,
        // 'username': username,
        // 'email':email,
        // 'number': number,
        // 'pickup':pickup,
        // 'message': message,
      }
      console.log(forward_data)
    //   SendAjax(forward_data);

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