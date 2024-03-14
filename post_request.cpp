#include <iostream>
#include <fstream>
#include "HTTPRequest.hpp"

int main() {
    try {
        int x = 1;
        int y = 2;
        int z = 3;
        // Construct the JSON string with variables
        std::string body = "{\"x\": " + std::to_string(x) + ", \"y\": " + std::to_string(y) + ", \"z\": " + std::to_string(z) + "}";
        http::Request request{"http://192.168.4.157:5000/api/resources/rgb"};
        const auto response = request.send("POST", body, {
            {"Content-Type", "application/json"}
        });
        std::cout << std::string{response.body.begin(), response.body.end()} << '\n'; // print the result
    }
    catch (const std::exception& e) {
        std::cerr << "Request failed, error: " << e.what() << '\n';
    }
    return 0;
}


// {'x': 150, 'y': 200, 'z': 300}