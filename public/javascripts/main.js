
const {jsPDF} = window.jspdf;

const scriptsCount = 1;
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
        <div class="card-body ${result.vulnerable?'text-danger':'text-success'}"> 
        <pre class="card-title">${result.title}</pre>
        <pre class="card-title">${result.summary}</pre> 
        <a  data-bs-toggle="collapse" href="#recommendation" role="button" aria-expanded="false" aria-controls="recommendation">
      + 
       </a>
       <div class="collapse" id="recommendation">
        <pre class="card-title">${result.recommendation}</pre> 
        <pre class="card-title">${result.vulnerable}</pre> 
       </div>
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
    const doc = new jsPDF();

    // Add cover page
    doc.setFontSize(24);
    doc.text("WORD PRESS VULNERABILITY SCAN REPORT", 20, 30);
    doc.setFontSize(16);
    doc.text("Confidential", 20, 50);
    doc.text(`Scan URL: ${urlInput.value.trim()}`, 20, 60);
    doc.text(`Scan Date: ${new Date().toLocaleDateString()}`, 20, 70);
    doc.addPage();

    // Add table of contents
    doc.setFontSize(20);
    doc.text("Table of Contents", 20, 20);
    doc.setFontSize(12);
    let y = 30;
    results.forEach((result, index) => {
      doc.text(`${index + 1}. ${result.script}`, 20, y);
      y += 10;
    });
    doc.addPage();

    // Add results with titles and content
    results.forEach((result, index) => {
      if (index > 0) {
        doc.addPage();
      }
      doc.setFontSize(18);
      doc.text(result.script, 20, 20);
      doc.setFontSize(12);
      y = 30;
      const lines = doc.splitTextToSize(result.message, 180);
      doc.text(lines, 20, y);
    });

    // Add footer to each page
    const pageCount = doc.internal.getNumberOfPages();
    for (let i = 1; i <= pageCount; i++) {
      doc.setPage(i);
      doc.setFontSize(10);
      doc.text(`Page ${i} of ${pageCount}`, 180, 290);
    }

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

