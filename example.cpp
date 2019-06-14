#include <iostream>
#include <opencv2/opencv.hpp>
#include <opencv2/highgui.hpp>

int main() {
	cv::Mat image(320, 240, CV_8UC3, cv::Scalar(0,0,0));
	cv::imwrite("test.jpg", image);
	std::cout << "saved image: test.jpg" << std::endl;
}
