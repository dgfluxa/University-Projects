# frozen_string_literal: true

require 'test_helper'

class StudyGroupsControllerTest < ActionDispatch::IntegrationTest
  test 'should get new' do
    get study_groups_new_url
    assert_response :success
  end

  test 'should get create' do
    get study_groups_create_url
    assert_response :success
  end

  test 'should get edit' do
    get study_groups_edit_url
    assert_response :success
  end

  test 'should get update' do
    get study_groups_update_url
    assert_response :success
  end

  test 'should get show' do
    get study_groups_show_url
    assert_response :success
  end

  test 'should get index' do
    get study_groups_index_url
    assert_response :success
  end

  test 'should get destroy' do
    get study_groups_destroy_url
    assert_response :success
  end
end
