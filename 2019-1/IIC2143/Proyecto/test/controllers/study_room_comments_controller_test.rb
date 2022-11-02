# frozen_string_literal: true

require 'test_helper'

class StudyRoomCommentsControllerTest < ActionDispatch::IntegrationTest
  test 'should get index' do
    get study_room_comments_index_url
    assert_response :success
  end

  test 'should get show' do
    get study_room_comments_show_url
    assert_response :success
  end

  test 'should get new' do
    get study_room_comments_new_url
    assert_response :success
  end

  test 'should get edit' do
    get study_room_comments_edit_url
    assert_response :success
  end

  test 'should get create' do
    get study_room_comments_create_url
    assert_response :success
  end

  test 'should get destroy' do
    get study_room_comments_destroy_url
    assert_response :success
  end

  test 'should get update' do
    get study_room_comments_update_url
    assert_response :success
  end
end
