#include <chrono>
#include <cinttypes>
#include <memory>
#include "minimal_interfaces/srv/add_three_ints.hpp"
#include "rclcpp/rclcpp.hpp"

using AddThreeInts = minimal_interfaces::srv::AddThreeInts;

int main(int argc, char *argv[])
{
    rclcpp::init(argc, argv);
    auto node = rclcpp::Node::make_shared("minimal_client");
    auto client = node->create_client<AddThreeInts>("add_three_ints");

    // wait for service
    while (!client->wait_for_service(std::chrono::seconds(1)))
    {
        if (!rclcpp::ok())
        {
            RCLCPP_ERROR(node->get_logger(), "client interrupted while waiting for service to appear.");
            return 1;
        }
        RCLCPP_INFO(node->get_logger(), "waiting for service to appear...");
    }

    auto request = std::make_shared<AddThreeInts::Request>();
    request->a = 41;
    request->b = 1;
    request->c = 2;
    auto result_future = client->async_send_request(request);
    if (rclcpp::spin_until_future_complete(node, result_future) !=
        rclcpp::executor::FutureReturnCode::SUCCESS)
    {
        RCLCPP_ERROR(node->get_logger(), "service call failed :(");
        return 1;
    }
    auto result = result_future.get();
    RCLCPP_INFO(node->get_logger(), "result of %" PRId64 " + %" PRId64 " + %" PRId64 "= %" PRId64,
                request->a, request->b, request->c, result->sum);
    rclcpp::shutdown();
    return 0;
}
