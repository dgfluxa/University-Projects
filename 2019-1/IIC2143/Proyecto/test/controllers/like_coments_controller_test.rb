# frozen_string_literal: true

require 'test_helper'

class LikeComentsControllerTest < ActionDispatch::IntegrationTest
  test 'should get destroy' do
    get like_coments_destroy_url
    assert_response :success
  end

  test 'should get create' do
    get like_coments_create_url
    assert_response :success
  end
end
