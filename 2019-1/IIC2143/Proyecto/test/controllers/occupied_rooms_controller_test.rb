# frozen_string_literal: true

require 'test_helper'

class OccupiedRoomsControllerTest < ActionDispatch::IntegrationTest
  test 'should get new' do
    get occupied_rooms_new_url
    assert_response :success
  end

  test 'should get create' do
    get occupied_rooms_create_url
    assert_response :success
  end

  test 'should get edit' do
    get occupied_rooms_edit_url
    assert_response :success
  end

  test 'should get update' do
    get occupied_rooms_update_url
    assert_response :success
  end

  test 'should get destroy' do
    get occupied_rooms_destroy_url
    assert_response :success
  end
end
