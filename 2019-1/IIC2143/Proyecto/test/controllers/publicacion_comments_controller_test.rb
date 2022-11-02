# frozen_string_literal: true

require 'test_helper'

class PublicacionCommentsControllerTest < ActionDispatch::IntegrationTest
  test 'should get new' do
    get publicacion_comments_new_url
    assert_response :success
  end

  test 'should get create' do
    get publicacion_comments_create_url
    assert_response :success
  end

  test 'should get edit' do
    get publicacion_comments_edit_url
    assert_response :success
  end

  test 'should get update' do
    get publicacion_comments_update_url
    assert_response :success
  end

  test 'should get index' do
    get publicacion_comments_index_url
    assert_response :success
  end

  test 'should get show' do
    get publicacion_comments_show_url
    assert_response :success
  end

  test 'should get destroy' do
    get publicacion_comments_destroy_url
    assert_response :success
  end
end
