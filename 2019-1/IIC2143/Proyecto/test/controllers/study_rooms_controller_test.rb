# frozen_string_literal: true

require 'test_helper'

class StudyRoomsControllerTest < ActionDispatch::IntegrationTest
  test 'should get index' do
    get study_rooms_index_url
    assert_response :success
  end

  test 'should get show' do
    get study_rooms_show_url
    assert_response :success
  end

  test 'should get new' do
    get study_rooms_new_url
    assert_response :success
  end

  test 'should get edit' do
    get study_rooms_edit_url
    assert_response :success
  end
end
