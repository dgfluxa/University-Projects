# frozen_string_literal: true

require 'test_helper'

class OfertclasesControllerTest < ActionDispatch::IntegrationTest
  test 'should get index' do
    get ofertclases_index_url
    assert_response :success
  end

  test 'should get new' do
    get ofertclases_new_url
    assert_response :success
  end

  test 'should get create' do
    get ofertclases_create_url
    assert_response :success
  end

  test 'should get destroy' do
    get ofertclases_destroy_url
    assert_response :success
  end

  test 'should get edit' do
    get ofertclases_edit_url
    assert_response :success
  end

  test 'should get update' do
    get ofertclases_update_url
    assert_response :success
  end

  test 'should get show' do
    get ofertclases_show_url
    assert_response :success
  end
end
