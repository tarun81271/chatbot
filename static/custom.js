function submit_message(message) {
        $.post( "/send_message", {message: message}, handle_response);

        function handle_response(data) {
          // append the bot repsonse to the div
          $('.chats').append(`
                <div class="client-chat col-md-5 offset-md-7 bot-message">
                    ${data.message}
                </div>
          `)
          // remove the loading indicator
          $( "#loading" ).remove();
        }
    }

$('#target').on('submit', function(e){
        e.preventDefault();
        const input_message = $('#input_message').val()
        // return if the user does not enter any text
        if (!input_message) {
          return
        }

        $('.chats').append(`
            <div class="client-chat col-md-5 human-message">
                ${input_message}
            </div>
        `)

        // loading 
        $('.chats').append(`
            <div class="client-chat text-center col-md-2 offset-md-10 bot-message" id="loading">
                <b>...</b>
            </div>
        `)

        // clear the text input 
        $('#input_message').val('')

        // send the message
        submit_message(input_message)
    });