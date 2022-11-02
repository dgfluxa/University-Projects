# frozen_string_literal: true

require 'test_helper'

class ImboxsControllerTest < ActionDispatch::IntegrationTest
  test 'should get index' do
    get imboxs_index_url
    assert_response :success
  end

  test 'should get update' do
    get imboxs_update_url
    assert_response :success
  end

  test 'should get destroy' do
    get imboxs_destroy_url
    assert_response :success
  end
end
