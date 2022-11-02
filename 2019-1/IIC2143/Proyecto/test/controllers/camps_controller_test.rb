# frozen_string_literal: true

require 'test_helper'

class CampsControllerTest < ActionDispatch::IntegrationTest
  test 'should get new' do
    get camps_new_url
    assert_response :success
  end

  test 'should get create' do
    get camps_create_url
    assert_response :success
  end

  test 'should get edit' do
    get camps_edit_url
    assert_response :success
  end

  test 'should get update' do
    get camps_update_url
    assert_response :success
  end

  test 'should get show' do
    get camps_show_url
    assert_response :success
  end

  test 'should get index' do
    get camps_index_url
    assert_response :success
  end

  test 'should get destroy' do
    get camps_destroy_url
    assert_response :success
  end
end
