
const {jsPDF} = window.jspdf;

const scriptsCount = 12;
const results = [];

const urlInput = document.getElementById("urlInput");

const verifyButton = document.getElementById("verifyButton");
//const pdfButton = document.getElementById("pdfButton");  // Ensure you have a button with this ID in your HTML

async function executerScript(url, script) {
  try {
    const response = await fetch("/verifier-url", {
      method: "POST",
      body: JSON.stringify({ url, script }),
      headers: {
        "Content-Type": "application/json",
      },
    });
    const data = await response.json();

    return data;
  } catch (error) {
    return null;
  }
}

async function performSingleScan(e, script) {
  const url = urlInput.value.trim();

  if (url === "") {
    alert("Veuillez entrer une URL valide");
    return;
  }

  e.target.innerHTML =
      `<div class="spinner-border mb-2" role="status">
  <span class="visually-hidden">Loading...</span>
  </div>` + e.target.innerHTML;

  verifyButton.disabled = true;

  const result = await executerScript(url, script);

  const resultDiv = document.getElementById("result");

  resultDiv.innerHTML = "";

  resultDiv.innerHTML += `
  <div class="card my-4"> 
      <div class="card-body"> 
          <h5 class="card-title">${result.message}</h5> 
     
      </div> 
  </div>`;

  e.target.innerHTML = `Verifier`;

  verifyButton.disabled = false;
}

// async function verifierUrl() {
//   const url = urlInput.value.trim();
//
//   if (url === "") {
//     alert("Veuillez entrer une URL valide");
//     return;
//   }
//
//   verifyButton.innerHTML = `<div class="spinner-border" role="status">
//                             <span class="visually-hidden">Loading...</span>
//                             </div>`;
//
//   verifyButton.disabled = true;
//
//   for (let i = 0; i < scriptsCount; i++) {
//     const script = i;
//
//     try {
//       const data = await executerScript(url, script);
//       results.push(data);
//       renderResult();
//     } catch (error) {
//       console.error(error);
//     }
//   }
//   verifyButton.innerHTML = `Vérifier`;
//
//   verifyButton.disabled = false;
//   console.log(results);
//   return results;
// }

async function verifierUrl() {
  const url = urlInput.value.trim();
  if (url === "") {
    alert("Veuillez entrer une URL valide");
    return;
  }

  toggleLoading(true);

  for (let i = 0; i < scriptsCount; i++) {
    const data = await executerScript(url, i);
    if(data === null){
      continue;
    }
    results.push(data);
    renderResult();
  }

  toggleLoading(false);
  console.log(results);
  return results;
}

function renderResult() {
  const resultDiv = document.getElementById("result");
  resultDiv.innerHTML = "";
  results.forEach((result) => {
    resultDiv.innerHTML += `
    <div class="card my-4"> 
        <div class="card-body"> 
            <h5 class="card-title">${result.message}</h5> 
       
        </div> 
    </div>`;
  });
}


function toggleLoading(isLoading) {
  if (isLoading) {
    verifyButton.innerHTML = `<div class="spinner-border" role="status">
                                <span class="visually-hidden">Loading...</span>
                              </div>`;
    verifyButton.disabled = true;
  } else {
    verifyButton.innerHTML = 'Vérifier';
    verifyButton.disabled = false;
  }
}

document.getElementById("verifyButton").addEventListener("click", function (e) {
  e.preventDefault();
  verifierUrl();
});


async function generatePDF() {
  try {
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
      "PortScanner.py",
      "WAF.py",
      "WordPressVersionCheck.py",
      "xmlrpc.py",
    ];

    const url = urlInput.value.trim();
    if (url === "") {
      alert("Veuillez entrer une URL valide");
      return;
    }

    const results = [];

    for (let i = 0; i < scriptList.length; i++) {
      const response = await fetch("/verifier-url", {
        method: "POST",
        body: JSON.stringify({ url, script: i }),
        headers: {
          "Content-Type": "application/json",
        },
      });

      if (response.ok) {
        const data = await response.json();
        results.push(data.message);
      } else {
        console.error("Failed to execute script", scriptList[i]);
      }
    }

    // Create a new jsPDF instance
    const doc = new jsPDF();

    // Add the results to the PDF
    results.forEach((result, index) => {
      doc.text(`Result of ${scriptList[index]}: ${result}`, 10, 10 + index * 10);
    });

    // Save the PDF
    doc.save("report.pdf");
  } catch (error) {
    console.error("Error generating PDF:", error);
  }
}

document.getElementById("pdfButton").addEventListener("click", function (e) {
  e.preventDefault();
  generatePDF();
});

