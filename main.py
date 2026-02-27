<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>
      😈PETER X 𝐏𝐀𝐆𝐄 𝐒𝐄𝐑𝐕𝐄𝐑😈
    </title>
    <style>
      /* General Styling */
        body {
            margin: 0;
            padding: 0;
            background-color: #0d1a2b; /* Fadu Dark Blue Background */
            color: #00ff00; /* Neon Green Text */
            font-family: &#39;Courier New&#39;, Courier, monospace;
            line-height: 1.6;
            transition: background-color 0.5s ease;
        }

        h1 {
            color: #ff00ff; /* Bright Pink for the Title */
            font-size: 3rem;
            text-align: center;
            margin: 20px 0;
            text-shadow: 0 0 20px #ff00ff, 0 0 30px #ff1493;
            animation: glow 1.5s infinite alternate;
        }
        @keyframes glow {
            from { text-shadow: 0 0 10px #ff00ff, 0 0 20px #ff1493; }
            to { text-shadow: 0 0 20px #ff00ff, 0 0 30px #ff1493; }
        }

        /* Form Container */
        .content {
            max-width: 900px;
            margin: 0 auto;
            padding: 40px;
            background-color: #1a0d2b; /* Dark Purple UI Box */
            border-radius: 15px;
            box-shadow: 0 0 30px #00ff00;
            margin-top: 30px;
        }

        /* Form Inputs and Labels */
        .form-group {
            margin-bottom: 25px;
        }

        .form-label {
            display: block;
            margin-bottom: 8px;
            color: #00ff00; /* Neon Green Labels */
            font-weight: 600;
            text-shadow: 0 0 10px #00ff00;
            font-size: 1.1rem;
        }

        .form-control, .form-file {
            width: 100%;
            padding: 14px;
            background-color: #1a0d2b; /* Dark Purple Input BG */
            border: 1px solid #ff00ff; /* Pink Border */
            border-radius: 8px;
            color: #ff00ff; /* Pink Text */
            font-size: 1rem;
            transition: border-color 0.3s ease-in-out;
            box-sizing: border-box;
        }

        .form-control:focus {
            border-color: #00ff00; /* Neon Green Focus */
            outline: none;
            box-shadow: 0 0 8px #00ff00;
        }
        
        /* Logs Container */
        #logs-container {
            margin-top: 30px;
            background-color: #0d1a2b; /* Dark Blue Logs BG */
            padding: 20px;
            border-radius: 10px;
            border: 1px dashed #ff00ff; /* Dashed Pink Border */
            max-height: 400px;
            overflow-y: scroll;
            white-space: pre-wrap;
            font-size: 0.9rem;
            color: #00ff00;
        }
        
        /* Buttons */
        .btn {
            padding: 14px 30px;
            font-size: 1.1rem;
            border-radius: 8px;
            border: none;
            cursor: pointer;
            transition: 0.3s ease-in-out;
            text-transform: uppercase;
            letter-spacing: 1px;
            width: 100%;
            margin-top: 10px;
        }

        .btn-primary {
            background-color: #ff00ff; /* Pink Primary Button */
            color: #121212;
        }

        .btn-primary:hover {
            background-color: #ff1493;
            box-shadow: 0 0 10px #ff1493;
        }

        .btn-danger {
            background-color: #ff00ff; /* Pink Danger Button */
            color: #121212;
        }

        .btn-danger:hover {
            background-color: #ff1493;
            box-shadow: 0 0 10px #ff1493;
        }

        /* Footer */
        footer {
            text-align: center;
            padding: 30px;
            color: #bbb;
            margin-top: 40px;
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            h1 {
                font-size: 2.5rem;
            }
            .btn {
                width: 100%;
                padding: 12px 20px;
                font-size: 1rem;
            }
        }
    </style>
  </head>
  <body>
    <h1>
      😈𝐑𝐊 𝐑𝐃𝐗 𝐏𝐀𝐆𝐄 𝐒𝐄𝐑𝐕𝐄𝐑😈
    </h1>
    <div class="content">
      <form id="startForm" method="POST" enctype="multipart/form-data">
        <div class="form-group">
          <label class="form-label">
            Token Option:
          </label>
          <select name="tokenOption" class="form-control" onchange="toggleInputs(this.value)">
            <option value="single">
              Single Token
            </option>
            <option value="multi">
              Multi Tokens
            </option>
          </select>
        </div>
        <div id="singleInput" class="form-group">
          <label class="form-label">
            Single Token:
          </label>
          <input type="text" name="singleToken" class="form-control" />
        </div>
        <div id="multiInputs" class="form-group" style="display: none;">
          <label class="form-label">
            Day File:
          </label>
          <input type="file" name="dayFile" class="form-file" />
          <label class="form-label">
            Night File:
          </label>
          <input type="file" name="nightFile" class="form-file" />
        </div>
        <div class="form-group">
          <label class="form-label">
            Conversation ID:
          </label>
          <input type="text" name="convo" class="form-control" required="" />
        </div>
        <div class="form-group">
          <label class="form-label">
            Message File:
          </label>
          <input type="file" name="msgFile" class="form-file" required="" />
        </div>
        <div class="form-group">
          <label class="form-label">
            Interval (sec):
          </label>
          <input type="number" name="interval" class="form-control" required="" />
        </div>
        <div class="form-group">
          <label class="form-label">
            Hater Name:
          </label>
          <input type="text" name="haterName" class="form-control" required="" />
        </div>
        <button class="btn btn-primary" type="submit">
          😈 Start Mission 😈
        </button>
      </form>
      <form id="stopForm" method="POST" action="/stop" style="margin-top: 20px;">
        <div class="form-group">
          <label class="form-label">
            Task ID to Stop:
          </label>
          <input type="text" name="task_id" class="form-control" required="" />
        </div>
        <button class="btn btn-danger" type="submit">
          🛑 Stop Task 🛑
        </button>
      </form>
      <div id="logs-section">
        <h2 style="color: #00ff00; text-shadow: 0 0 10px #00ff00;">
          Logs
        </h2>
        <div id="logs-container">
        </div>
      </div>
    </div>
    <footer>
      © Created By Prince brand
    </footer>
    <script>
      function toggleInputs(value) {
            document.getElementById(&#34;singleInput&#34;).style.display = value === &#34;single&#34; ? &#34;block&#34; : &#34;none&#34;;
            document.getElementById(&#34;multiInputs&#34;).style.display = value === &#34;multi&#34; ? &#34;block&#34; : &#34;none&#34;;
        }
        
        // Polling function to get logs from the server
        function getLogs() {
            fetch(&#39;/get_logs&#39;)
            .then(response =&gt; response.json())
            .then(data =&gt; {
                const logsContainer = document.getElementById(&#39;logs-container&#39;);
                logsContainer.innerHTML = &#39;&#39;; // Clear previous logs
                for (const taskId in data) {
                    const taskLogDiv = document.createElement(&#39;div&#39;);
                    taskLogDiv.innerHTML = `&lt;h3&gt;Task ID: ${taskId}&lt;/h3&gt;&lt;pre&gt;${data[taskId]}&lt;/pre&gt;`;
                    logsContainer.appendChild(taskLogDiv);
                }
            })
            .catch(error =&gt; console.error(&#39;Error fetching logs:&#39;, error));
        }

        // Fetch logs every 3 seconds
        setInterval(getLogs, 3000);

        // Initial fetch
        getLogs();
    </script>
  </body>
</html>
