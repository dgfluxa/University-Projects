# frozen_string_literal: true

require 'test_helper'

class StudyRoomValorationsControllerTest < ActionDispatch::IntegrationTest
  test 'should get new' do
    get study_room_valorations_new_url
    assert_response :success
  end

  test 'should get create' do
    get study_room_valorations_create_url
    assert_response :success
  end

  test 'should get edit' do
    get study_room_valorations_edit_url
    assert_response :success
  end

  test 'should get update' do
    get study_room_valorations_update_url
    assert_response :success
  end

  test 'should get destroy' do
    get study_room_valorations_destroy_url
    assert_response :success
  end
end
