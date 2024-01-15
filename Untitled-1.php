<?php

function encrypt_json($json_data, $watermark) {
    // Hash the watermark
    $hash_watermark = hash("sha256", $watermark);

    // Generate the encryption key
    $key = openssl_random_pseudo_bytes(32);

    // Encrypt the data
    $cipher = openssl_encrypt($json_data, "AES-256-CTR", $key, OPENSSL_RAW_DATA, $hash_watermark);

    // Encode the encrypted data to base64
    $encoded_data = base64_encode($cipher);

    return $encoded_data;
}


function main() {
    // Get the JSON data
    $json_data = file_get_contents("data.json");

    // Get the watermark
    $watermark = "My secret watermark";

    // Encrypt the JSON data
    $encrypted_data = encrypt_json($json_data, $watermark);

    // Save the encrypted data
    file_put_contents("encrypted_data.json", $encrypted_data);
}


if (isset($_POST["submit"])) {
    main();
}
?>
