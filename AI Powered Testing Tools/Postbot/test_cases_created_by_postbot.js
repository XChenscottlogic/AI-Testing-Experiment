pm.test("Response status code is 200", function () {
    pm.expect(pm.response.code).to.eql(201);
});

pm.test("Response time is less than 200ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(200);
});

pm.test("Response has the required fields", function () {
    const responseData = pm.response.json();
    
    pm.expect(responseData).to.be.an('object');
    pm.expect(responseData).to.have.all.keys('generated_text', 'token_count', 'model', 'timestamp');
});

pm.test("Token count is a non-negative integer", function () {
    const responseData = pm.response.json();
    
    pm.expect(responseData).to.be.an('object');
    pm.expect(responseData.token_count).to.be.a('number').and.to.be.at.least(0);
});

pm.test("Timestamp is in a valid date-time format", function () {
    const responseData = pm.response.json();
    
    pm.expect(responseData).to.be.an('object');
    pm.expect(responseData.timestamp).to.exist;
    pm.expect(new Date(responseData.timestamp).getTime()).to.not.be.NaN;
});
pm.test("Status code is 200", function () {
    pm.expect(pm.response.code).to.equal(200);
});
pm.test("Response schema is valid", function () {
    const responseData = pm.response.json();
    
    pm.expect(responseData).to.have.property('generated_text').that.is.a('string');
    pm.expect(responseData).to.have.property('token_count').that.is.a('number');
    pm.expect(responseData).to.have.property('model').that.is.a('string');
    pm.expect(responseData).to.have.property('timestamp').that.is.a('string');
});
var responseData = pm.response.json();

// Test for response status code
pm.test("Response status code is 200", function () {
    pm.expect(pm.response.code).to.eql(200);
});

// Test for response time
pm.test("Response time is less than 200ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(200);
});

// Test for required fields in response
pm.test("Response has the required fields", function () {
    pm.expect(responseData).to.be.an('object').that.has.all.keys('generated_text', 'token_count', 'model', 'timestamp');
});

// Test for token count being a non-negative integer
pm.test("Token count is a non-negative integer", function () {
    pm.expect(responseData.token_count).to.be.a('number').and.to.be.at.least(0);
});

// Test for timestamp format
pm.test("Timestamp is in a valid date-time format", function () {
    pm.expect(responseData.timestamp).to.exist;
    pm.expect(new Date(responseData.timestamp).getTime()).to.not.be.NaN;
});

// Test for length of generated_text
pm.test("Generated text length is greater than 0", function () {
    pm.expect(responseData.generated_text.length).to.be.greaterThan(0, "Generated text should not be empty");
});

// Test for response schema validation
pm.test("Response schema is valid", function () {
    pm.expect(responseData).to.have.property('generated_text').that.is.a('string');
    pm.expect(responseData).to.have.property('token_count').that.is.a('number');
    pm.expect(responseData).to.have.property('model').that.is.a('string');
    pm.expect(responseData).to.have.property('timestamp').that.is.a('string');
});
var responseData = pm.response.json();

// Combine existing tests for response structure and schema validation
pm.test("Response structure and schema are valid", function () {
    pm.expect(responseData).to.be.an('object').that.has.all.keys('generated_text', 'token_count', 'model', 'timestamp');
    pm.expect(responseData.generated_text).to.be.a('string');
    pm.expect(responseData.token_count).to.be.a('number').and.to.be.at.least(0);
    pm.expect(responseData.model).to.be.a('string');
    pm.expect(responseData.timestamp).to.be.a('string');
});

// Test for length of generated_text
pm.test("Generated text length is greater than 0", function () {
    pm.expect(responseData.generated_text.length).to.be.greaterThan(0, "Generated text should not be empty");
});

var template = `
<style type="text/css">
    .tftable {font-size:14px;color:#333333;width:100%;border-width: 1px;border-color: #87ceeb;border-collapse: collapse;}
    .tftable th {font-size:18px;background-color:#87ceeb;border-width: 1px;padding: 8px;border-style: solid;border-color: #87ceeb;text-align:left;}
    .tftable tr {background-color:#ffffff;}
    .tftable td {font-size:14px;border-width: 1px;padding: 8px;border-style: solid;border-color: #87ceeb;}
    .tftable tr:hover {background-color:#e0ffff;}
</style>

<table class="tftable" border="1">
    <tr>
        <th>Generated Text</th>
        <th>Token Count</th>
        <th>Model</th>
        <th>Timestamp</th>
    </tr>
    <tr>
        <td>{{response.generated_text}}</td>
        <td>{{response.token_count}}</td>
        <td>{{response.model}}</td>
        <td>{{response.timestamp}}</td>
    </tr>
</table>
`;

function constructVisualizerPayload() {
    return { response: pm.response.json() };
}

pm.visualizer.set(template, constructVisualizerPayload());
// Store generated_text in a global variable for later use
  var responseData = pm.response.json();
pm.globals.set("generatedText", responseData.generated_text);

pm.test("Response headers include Content-Type as application/json", function () {
    pm.expect(pm.response.headers.get('Content-Type')).to.eql('application/json');
});


pm.test("Generated text must be a non-null string", function () {
    const responseData = pm.response.json();
    
    pm.expect(responseData).to.be.an('object');
    pm.expect(responseData.generated_text).to.exist.and.to.be.a('string').and.to.not.be.empty;
});


pm.test("Model field is a valid string with specific expected values", function () {
    const responseData = pm.response.json();
    
    pm.expect(responseData).to.be.an('object');
    pm.expect(responseData.model).to.be.a('string').that.is.not.empty;
    const validModels = ["modelA", "modelB", "modelC"];
    pm.expect(validModels).to.include(responseData.model);
});


pm.test("Timestamp is not in the future", function () {
    const responseData = pm.response.json();
    pm.expect(new Date(responseData.timestamp)).to.be.at.most(new Date(), "Timestamp should not be in the future");
});


pm.test("Token count is less than or equal to the length of generated text", function () {
    const responseData = pm.response.json();
    
    pm.expect(responseData).to.be.an('object');
    pm.expect(responseData.token_count).to.be.at.most(responseData.generated_text.length);
});

pm.test("Response headers include Content-Type as application/json", function () {
    pm.expect(pm.response.headers.get('Content-Type')).to.eql('application/json');
});


// Store the 'model' field in a global variable for later use
var responseData = pm.response.json();
pm.globals.set("modelField", responseData.model);

pm.test("Response headers include Content-Length header", function () {
    pm.expect(pm.response.headers.has('Content-Length')).to.be.true;
});


pm.test("The generated text length must not exceed 500 characters", function () {
    const responseData = pm.response.json();
    
    pm.expect(responseData).to.be.an('object');
    pm.expect(responseData.generated_text).to.exist.and.to.have.lengthOf.at.most(500, "Generated text exceeds maximum length");
});


pm.test("Response body is not empty", function () {
    const responseData = pm.response.json();
    
    pm.expect(responseData).to.be.an('object');
    pm.expect(Object.keys(responseData)).to.have.lengthOf.above(0; // Ensure the object has keys
    pm.expect(responseData.generated_text).to.exist.and.to.have.lengthOf.at.least(1, "Generated text should not be empty");
});


pm.test("Model field matches expected format", function () {
    const responseData = pm.response.json();
    
    pm.expect(responseData).to.be.an('object');
    pm.expect(responseData.model).to.exist.and.to.match(/^model/);
});


pm.test("Token count does not exceed predefined maximum value", function () {
    const responseData = pm.response.json();
    
    pm.expect(responseData).to.have.property('token_count').that.is.a('number').and.is.at.most(1000); // Replace 1000 with the predefined maximum value
});

