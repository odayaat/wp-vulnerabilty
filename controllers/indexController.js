const { exec } = require("child_process");

const { PythonShell } = require("python-shell");

exports.getIndex = (req, res) => {
  res.render("index");
};

exports.postUrl = async (req, res) => {
  const { url, script } = req.body;

  // const script = "check_wp_admin.py";

  const scriptList = [
    "AccessiblePages.py",
    "BruteForce.py",
    "check_wp_admin.py",
    "CORS.py",
    "DirectoryListening.py",
    "FindingUsers.py",
    "GetPlugins.py",
    "Getthemes.py",
    "HeadersInfoDisclosure.py",
    "MissingSecurityHeaders.py",
   // "Port Scanner.py",
    //"URLcheck",
    "UserEnumeration.py",
    "ValidSSLCertificate.py",
    "WAF.py",
    "WordPressVersionCheck.py",
    "wp-admin.py",
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
  

 
   const jsonresult = JSON.parse(result[0]);
  //const resultObject = JSON.parse(result[0]);

  console.log(jsonresult);
  res.status(200).json(jsonresult);
};
