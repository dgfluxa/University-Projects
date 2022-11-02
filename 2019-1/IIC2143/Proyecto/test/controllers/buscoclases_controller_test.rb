# frozen_string_literal: true

require 'test_helper'

class BuscoclasesControllerTest < ActionDispatch::IntegrationTest
  test 'should get index' do
    get buscoclases_index_url
    assert_response :success
  end

  test 'should get create' do
    get buscoclases_create_url
    assert_response :success
  end

  test 'should get show' do
    get buscoclases_show_url
    assert_response :success
  end

  test 'should get destroy' do
    get buscoclases_destroy_url
    assert_response :success
  end
end
