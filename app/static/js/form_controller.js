const textFields = [].slice.call(document.querySelectorAll('.mdc-text-field'))
let materialAddressField;
let materialNumberField;
let materialComplementField;
const snackbar = mdc.snackbar.MDCSnackbar.attachTo(document.querySelector('.mdc-snackbar'));

textFields.forEach((textFieldEl, index) => {
    switch (index) {
        case 3:
            materialAddressField = mdc.textField.MDCTextField.attachTo(textFieldEl);
        case 4:
            materialNumberField = mdc.textField.MDCTextField.attachTo(textFieldEl);
        case 5:
            materialComplementField = mdc.textField.MDCTextField.attachTo(textFieldEl);
        default:
            mdc.textField.MDCTextField.attachTo(textFieldEl);
    }
})
const cepField = document.getElementById('cep');
let addressInfo;

let cepString = ""
cepField.addEventListener('change', (e) => {
    let baseApiURL = "https://viacep.com.br/ws/"
    const value = e.target.value;
    if (value.length >= 8 && value.length < 10) {
        cepString = value;
        if (value.includes('-')) {
            cepString = value.split('-').join('');
        }
        console.log(cepString);
        baseApiURL += (cepString + "/json/")
        console.log("BASE API URL: ", baseApiURL)
    }
    fetch(baseApiURL)
        .then(res => res.json())
        .then(json => {
            addressInfo = json
            if (json.logradouro !== undefined && json.logradouro !== 'undefined') {
                materialAddressField.value = addressInfo.logradouro;
                materialComplementField.value = addressInfo.complemento;
            } else {
                snackbar.open();
            }
            return
        })
        .then(() => {
            materialNumberField.focus();
        })
        .catch(e => {
            console.error(e);
            snackbar.open()
        })
})