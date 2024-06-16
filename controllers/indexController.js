const { exec } = require("child_process");

const { PythonShell } = require("python-shell");

exports.getIndex = (req, res) => {
  res.render("index");
};

exports.postUrl = async (req, res) => {
  const { url, script } = req.body;

  // const script = "check_wp_admin.py";

  const scriptList = [
      "check_wp_admin.py",
      "AccessiblePages.py",
      "CORS.py",
     "DirectoryListening.py",
     "FindingUsers.py",
      "GetPlugins.py",
      "Getthemes.py",
      "HeadersInfoDisclosure.py",
       "MissingSecurityHeaders.py",
     //  "URLcheck",
    "Port Scanner.py",
     "WAF.py",
      "WordPressVersionCheck.py",
     //"wp-admin",
    "xmlrpc.py",
  ];

  let options = {
    mode: "text",
    pythonPath: "C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python312\\python.exe",
    pythonOptions: ["-u"], // get print results in real-time
    scriptPath: "script",
    args: [url],
  };

  const result = await PythonShell.run(scriptList[script], options);
  console.log(result);

 

  //const resultObject = JSON.parse(result[0]);

  res.status(200).json({ message: result[0] });
};
