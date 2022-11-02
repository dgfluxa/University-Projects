# frozen_string_literal: true

require 'test_helper'

class SubscribedUsersControllerTest < ActionDispatch::IntegrationTest
  test 'should get update' do
    get subscribed_users_update_url
    assert_response :success
  end
end
