- name: Obtener UUID del paquete desde JSON local
  id: obtener_uuid
  run: |
    deployment_uuid=$(jq -r 'to_entries[] | .value as $app | select($app | has("${{ github.event.inputs.package_name }}")) | $app["${{ github.event.inputs.package_name }}"]' config/packages_result.json)
    echo "UUID resuelto: $deployment_uuid"
    echo "deployment_uuid=$deployment_uuid" >> $GITHUB_OUTPUT