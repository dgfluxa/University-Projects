# frozen_string_literal: true

require 'test_helper'

class ModerationRequestsControllerTest < ActionDispatch::IntegrationTest
  test 'should get new' do
    get moderation_requests_new_url
    assert_response :success
  end

  test 'should get edit' do
    get moderation_requests_edit_url
    assert_response :success
  end

  test 'should get show' do
    get moderation_requests_show_url
    assert_response :success
  end

  test 'should get create' do
    get moderation_requests_create_url
    assert_response :success
  end

  test 'should get destroy' do
    get moderation_requests_destroy_url
    assert_response :success
  end
end
